#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for python-schema_registry."""

from setuptools import find_packages, setup

__version__ = "1.4.2"

with open("README.md") as readme_file:
    long_description = readme_file.read()

requires = ["fastavro==0.24.0", "httpx==0.14.1"]

description = """Python Rest Client to interact against Schema Registry \
    Confluent Server to manage Avro Schemas
"""

setup(
    name="python-schema-registry-client",
    version=__version__,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marcos Schroh",
    author_email="schrohm@gmail.com",
    install_requires=requires,
    extras_require={
        "faust": ["faust==1.10.4",],
        "docs": ["mkdocs==1.1.2", "mkdocs-material==5.5.6",],
        "tests": [
            "black==19.10b0",
            "autoflake==1.3.1",
            "flake8==3.8.3",
            "mypy==0.782",
            "isort==5.4.1",
            "pytest==6.0.1",
            "pytest-mock==3.2.0",
            "faker==4.1.1",
            "codecov==2.1.8",
            "pytest-cov==2.10.0",
        ],
    },
    url="https://github.com/marcosschroh/python-schema-registry-client",
    download_url="https://pypi.org/project/python-schema-registry-client/#files",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        Schema Registry, Python, Avro, Apache, Apache Avro
        """
    ),
)
