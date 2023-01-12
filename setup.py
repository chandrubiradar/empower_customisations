from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in empower_customisations/__init__.py
from empower_customisations import __version__ as version

setup(
	name="empower_customisations",
	version=version,
	description="Empower Customisations app",
	author="Chandru",
	author_email="chandrucb95@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
