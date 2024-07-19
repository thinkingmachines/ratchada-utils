#!/usr/bin/env python
#
# RATCHADA_UTILS: PROCESSOR PACKAGE
#
# COPYRIGHT (C) 2024 RATCHADA UTILS PROJECT
# AUTHOR:   TM-BEST-CHOKULKET
#           TM-ZOON-PATCHARAWIWATPONG
# URL: <https://thinkingmachin.es/>
# LICENSE: see LICENSE for further info

from setuptools import find_packages, setup
import os
from setuptools_scm import get_version
from setuptools_scm.version import guess_next_version


def version_scheme(version):
    if version.exact:
        return version.format_with("{tag}")
    else:
        return guess_next_version(version.tag)


def parse_requirements(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


with open("README.md", encoding="utf-8") as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="ratchada-utils",
    use_scm_version={
        "write_to": "ratchada_utils/VERSION",
        "write_to_template": "{version}",
        "version_scheme": version_scheme,
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools", "setuptools_scm"],
    packages=find_packages(where="ratchada_utils"),
    package_dir={"": "ratchada_utils"},
    url="https://github.com/thinkingmachines/ratchada-utils/",
    project_urls={
        "Documentation": "https://huggingface.co/ThinkingMachinesDataScience/Ratchada-Fang-Thon-Whisper",
        "Source Code": "https://github.com/thinkingmachines/ratchada-utils",
        "Issue Tracker": "https://github.com/thinkingmachines/ratchada-utils/issues",
    },
    description="Ratchada Utils are Python package use with Ratchada Whisper model utilities.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=[
        "model",
        "Ratchada-Whisper",
        "tokenizing",
        "language",
        "natural language",
        "text analytics",
    ],
    maintainer="Thinking Machines Data Sciences Inc. Thailand Team",
    maintainer_email="hello@thinkingmachin.es",
    author="tm-zoon",
    author_email="zoon_p@thinkingmachin.es",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
    ],
    package_data={"ratchada_utils": ["test/*.doctest", "VERSION"]},
    python_requires=">=3.10, <3.12",
    install_requires=parse_requirements("requirements.txt"),
    zip_safe=False,
)
