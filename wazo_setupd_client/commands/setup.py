# -*- coding: utf-8 -*-
# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SetupdCommand

DEFAULT_TIMEOUT = 60


class SetupCommand(SetupdCommand):

    resource = 'setup'
    _headers = {'Content-Type': 'application/json',
                'Accept': 'application/json'}

    def create(self, body, timeout=DEFAULT_TIMEOUT):
        r = self.session.post(self.base_url, json=body, headers=self._headers, timeout=timeout)
        self.raise_from_response(r)
