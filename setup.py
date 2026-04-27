from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fitness_wellness/__init__.py
from fitness_wellness import __version__ as version

setup(
	name="fitness_wellness",
	version=version,
	description="Fitness & Wellness Management System",
	author="Antigravity",
	author_email="antigravity@google.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
