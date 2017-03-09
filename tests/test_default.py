from pytest import fixture


grafana_admin_user = "admin"
grafana_admin_password = "idrcidrc"


# Adapted from
# http://www.axelspringerideas.de/blog/index.php/2016/08/16/continuously-delivering-infrastructure-part-1-ansible-molecule-and-testinfra/
@fixture()
def Repository_exists(Command):
    """
    Tests if YUM Repo with specific Name exists and is enabled:
    - **repo** - repo name to look for
    **returns** - True if String is found
    """
    def f(repo):
        return (repo in Command.check_output("yum repolist"))
    return f


def test_grafana_repo_is_installed(Repository_exists):
    assert Repository_exists("Grafana upstream yum repo")


def test_grafana_package_is_installed(Package):
    pkg = Package("grafana")
    assert pkg.is_installed


def test_gedash_js_is_installed(File):
    assert File("/usr/share/grafana/public/dashboards/getdash.js").exists


def test_grafana_api_accepts_our_password(Command, TestinfraBackend):
    hostname = TestinfraBackend.get_hostname()
    url = "%s:%s@%s:3000/api/org" % (grafana_admin_user, grafana_admin_password, hostname)
    # This is the simplest one-liner I could find to GET a url and return just
    # the status code.
    # http://superuser.com/questions/590099/can-i-make-curl-fail-with-an-exitcode-different-than-0-if-the-http-status-code-i
    cmd = Command("curl --silent --output /dev/stderr --write-out '%%{http_code}' %s" % url)
    # Expect a 2xx status code.
    assert cmd.stdout.startswith("2")


def test_grafana_has_influxdb_datasource(Command, TestinfraBackend):
    hostname = TestinfraBackend.get_hostname()
    url = "%s:%s@%s:3000/api/datasources" % (grafana_admin_user, grafana_admin_password, hostname)
    cmd = Command("curl --silent %s" % url)
    assert '"name":"collectd (managed by ansible)"' in cmd.stdout
