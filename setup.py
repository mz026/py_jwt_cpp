# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_jwt_cpp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py_jwt_cpp',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Yanghsing Lin',
    'author_email': 'yanghsing.lin@gmail.com',
    'maintainer': 'Yanghsing Lin',
    'maintainer_email': 'yanghsing.lin@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
