from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in skyway/__init__.py
from skyway import __version__ as version

setup(
	name='skyway',
	version=version,
	description='customizations',
	author='Connect 4 systems',
	author_email='info@connect4systems.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
