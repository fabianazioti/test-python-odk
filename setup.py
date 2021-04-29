import os
from setuptools import find_packages, setup

tests_require = [
    'pytest>=5.2',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
]

extras_require = {
    'tests': tests_require,
}

extras_require['all'] = [ req for exts, reqs in extras_require.items() for req in reqs ]


install_requires = [
    'flask',
]

packages = find_packages()

setup(
    name='teste',
    packages=packages,
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
)
