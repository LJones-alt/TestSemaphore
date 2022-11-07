#!/usr/bin/python


from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(argument_spec={})
    returnValue = {"hello" : "Ansible"}
    module.exit_json(changed="false", meta=returnValue)


if __name__ == '__main__':
    main()