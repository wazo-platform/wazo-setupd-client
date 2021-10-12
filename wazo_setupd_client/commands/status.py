# Copyright 2018-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_setupd_client.command import SetupdCommand


class StatusCommand(SetupdCommand):

    resource = 'status'

    def get(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()
