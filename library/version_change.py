#!/usr/bin/python

## This will update a version number

from ansible.module_utils.basic import *

def main():

    fields = {
        "version_no": {"default": True, "type": "str"},
        "version_name": {"default": True, "type": "str"},
        "unchanged_value": {"default": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=fields)
    ## change the name
    module.params.update({"version_name": "After"})
    ## add to the version list - minor and patch
    version_list = module.params["version_no"].split('.')
    version_list[2] = str(int(version_list[2]) + 2)
    version_list[1] = str(int(version_list[1]) + 1)
    ## join the string back together
    version_string= '.'.join(version_list)
    module.params.update({"version_no": version_string})

    
    module.exit_json(changed=True, meta=module.params)


if __name__ == '__main__':
    main()