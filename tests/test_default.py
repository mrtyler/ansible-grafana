from pytest import fixture
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


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
