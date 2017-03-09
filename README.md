Ansible role: grafana
=========

Minimal Ansible role to manage grafana on CentOS 7.3.

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x
 * systemd

Role Variables
--------------

Grafana admin user. Used for authenticating to Grafana API.

    grafana_admin_user: admin

Grafana admin default password, i.e. out-of-the-box password. This will be changed to ``grafana_admin_password``.

    grafana_admin_default_password: admin

Grafana admin password

    grafana_admin_password: idrcidrc

File written when default password is changed

    grafana_admin_password_is_changed_file: /usr/share/grafana/admin_password_is_changed

Directory where getdash.js repo (including its install script) is fetched

    grafana_getdash_js_dest: /tmp/getdash_js

getdash.js upstream repo

    grafana_getdash_js_repo: https://github.com/anryko/grafana-influx-dashboard.git

getdash.js version (git sha from ``grafana_getdash_js_repo``)

    grafana_getdash_js_sha: ae111e53ae5f3ef8d2570439d26d905612ee223e  # master as of 2017-03-01

Name given to influxdb datasource. If a datasource with this name already exists, ansible will not attempt to re-add it.

    grafana_influxdb_datasource_name: collectd (managed by ansible)

Influxdb user

    grafana_influxdb_user: root

Influxdb password

    grafana_influxdb_password: root

Grafana version to install

    grafana_package_version: 4.1.2

Grafana packages (including helper packages) to install

    grafana_packages:
    - "grafana-{{ grafana_package_version }}"
    - git  # Needed for installing getdash.js

Port where Grafana server listens

    grafana_port: 3000

Grafana yum repo information

    grafana_repo: https://packagecloud.io/grafana/stable/el/$releasever/$basearch
    grafana_repo_key: https://grafanarel.s3.amazonaws.com/RPM-GPG-KEY-grafana

Where Grafana helpers, such as scripted dashboards like getdash.js, are installed

    grafana_root_dir: /usr/share/grafana


Example Playbook
----------------

    - hosts: servers
      roles:
        - ansible-role-grafana
          grafana_package_version: 1.2.0

Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role.

Because this role depends on systemd and might one day need SELinux (as related role ansible-influxdb does), only a Vagrant provider is configured at the moment.

License
-------

MIT

Author Information
------------------

Raising the Floor - US
