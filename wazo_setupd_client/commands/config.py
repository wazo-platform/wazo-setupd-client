# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from xivo_lib_rest_client import RESTCommand


class ConfigCommand(RESTCommand):

    resource = 'config'
    _headers = {'Accept': 'application/json'}

    def get(self):
        r = self.session.get(self.base_url, headers=self._headers)
        self.raise_from_response(r)
        return r.json()
