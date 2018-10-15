import os
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

varsfn = '../../defaults/main.yml'
with open(varsfn, 'r') as stream:
    defaults = yaml.load(stream)


def test_service(host):
    svc = host.service('apt-cacher-ng')

    assert svc.is_running
    assert svc.is_enabled


def test_cache_directory(host):
    dir = host.file(defaults['apt_cacher_ng_cache_dir'])
    assert dir.is_directory

# socket depends on netstat being installed - sad
# def test_port_listening(host):
#     port = defaults['apt_cacher_ng_port']
#     assert host.socket("tcp://0.0.0.0:%s" % port).is_listening
