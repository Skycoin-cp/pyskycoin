# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.26.0
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301
from codecs import open
from os import path

NAME = "skyapi"
VERSION = "0.25.1.post6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

script_dirname = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(script_dirname, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Skycoin REST API.",
    author_email="contact@skycoin.net",
    url="",
    keywords="skycoin crypto coin currency blockchain REST API",
    setup_requires=["pytest-runner"],
    tests_require=REQUIRES,
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
