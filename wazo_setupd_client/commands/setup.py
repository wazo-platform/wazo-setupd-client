# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from ..command import SetupdCommand

DEFAULT_TIMEOUT = 60


class SetupCommand(SetupdCommand):

    resource = 'setup'
    _headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    def create(self, body, timeout=DEFAULT_TIMEOUT):
        headers = self._get_headers()
        r = self.session.post(
            self.base_url, json=body, headers=headers, timeout=timeout
        )
        self.raise_from_response(r)
