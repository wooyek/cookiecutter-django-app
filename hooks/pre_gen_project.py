import re
import shutil
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('pre_gen_project')

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_name = '{{ cookiecutter.package_name}}'


if __name__ == '__main__':
    if not re.match(MODULE_REGEX, package_name):
        print('ERROR: The package name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % package_name)

        # Exit to cancel project
        sys.exit(1)

