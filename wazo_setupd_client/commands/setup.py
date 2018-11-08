# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from ..command import SetupdCommand


class SetupCommand(SetupdCommand):

    resource = 'setup'
    _headers = {'Content-Type': 'application/json',
                'Accept': 'application/json'}

    def create(self, body):
        r = self.session.post(self.base_url, json=body, headers=self._headers)
        self.raise_from_response(r)
