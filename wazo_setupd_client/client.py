# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from xivo_lib_rest_client.client import BaseClient


class SetupdClient(BaseClient):

    namespace = 'wazo_setupd_client.commands'

    def __init__(self,
                 host,
                 port=9302,
                 version='1.0',
                 **kwargs):
        super(SetupdClient, self).__init__(
            host=host,
            port=port,
            version=version,
            **kwargs)
