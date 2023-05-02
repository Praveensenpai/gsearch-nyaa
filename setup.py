from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.call(["playwright", "install", "chromium"])


setup(
    name="gsearch-nyaa",
    version="0.1.4",
    author="Praveen Senpai",
    author_email="pvnt20@gmail.com",
    description="A Python Package for Automated Google Searches and Scraping of Search Results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "selectolax",
    ],
    cmdclass={
        "install": CustomInstallCommand,
    },
)
