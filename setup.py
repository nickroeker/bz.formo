# Copyright 2019 Nicholas Kroeker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup file for Bluzelle Formo - An Unofficial Bluzelle Swarm Manager."""



from os import path
from setuptools import find_namespace_packages
from setuptools import setup

cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

version = "0.1.0.dev0"

name = "bz.formo"
description = "An Unofficial Bluzelle Swarm Manager."
long_description_content_type = "text/markdown"
url = "https://github.com/nickroeker/bz.formo"
author = "Nic Kroeker"
licenze = "Apache 2.0"
packages = find_namespace_packages(include=["bz.*"])

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development :: Testing :: Acceptance",
]

install_requires = []
extras_require = {"dev": ["pytest"]}

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url=url,
    author=author,
    license=licenze,
    packages=packages,
    classifiers=classifiers,
    install_requires=install_requires,
    extras_require=extras_require,
)
