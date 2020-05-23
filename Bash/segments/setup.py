# Copyright (c) 2020 Matheus Castello
# MicroHobby licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.

import setuptools

setuptools.setup(
    name="mysegments",
    version="0.0.1",
    author="Matheus Castello",
    author_email="matheus@castello.eng.br",
    description="My custom Powerline segments.",
    long_description="Segments for Docker info (docker images, docker ps), " + \
        "Git info (how many files are modified), random emojis for command errors",
    long_description_content_type="text/plain",
    packages=setuptools.find_packages(),
)
