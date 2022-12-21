#!/usr/bin/env python3
# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_setupd_client',
    version='1.0',
    description='a simple client library for the wazo setupd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_setupd_client.commands': [
            'config = wazo_setupd_client.commands.config:ConfigCommand',
            'setup = wazo_setupd_client.commands.setup:SetupCommand',
            'status = wazo_setupd_client.commands.status:StatusCommand',
        ],
    },
)
