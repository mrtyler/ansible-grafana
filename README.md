Ansible role: grafana
=========

Minimal Ansible role to manage grafana on CentOS 7.3.

Requirements
------------

 * CentOS 7.x
 * Ansible 2.x
 ??? * systemd

Role Variables
--------------

```
```

Dependencies
------------

??? * ansible-collectd - https://github.com/idi-ops/ansible-collectd

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-role-grafana
           grafana_package_version: 1.2.0

Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role.

Because this role depends on systemd and ??? SELinux, only a Vagrant provider is configured at the moment.

License
-------

MIT

Author Information
------------------

Raising the Floor - US
