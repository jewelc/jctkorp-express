from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jctkorp_express/__init__.py
from jctkorp_express import __version__ as version

setup(
	name="jctkorp_express",
	version=version,
	description="Jctkorp Express Services",
	author="jctkorp.com",
	author_email="info@jctkorp.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
