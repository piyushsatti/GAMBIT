# Some license :D

import os
import sys
import platform

# UPDATE_IF_PYTHON_VERSION_ADDED_OR_REMOVED : search for this string in codebase 
# when support for a Python version must be added or removed
_supported_versions = ['2.7', '3.6', '3.7', '3.8', '3.9']
_ver = sys.version_info
_version = '{0}.{1}'.format(_ver[0], _ver[1])
if not _version in _supported_versions:
    raise EnvironmentError('MATLAB Engine for Python supports Python version'
                           ' 2.7, 3.6, 3.7, and 3.8, but your version of Python '
                           'is %s' % _version)