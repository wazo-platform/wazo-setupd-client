#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


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
            'status = wazo_setupd_client.commands.status:StatusCommand',
        ],
    }
)
