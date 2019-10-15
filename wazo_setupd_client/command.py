# -*- coding: utf-8 -*-
# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import SetupdError
from .exceptions import SetupdSetupError
from .exceptions import SetupdServiceUnavailable
from .exceptions import InvalidSetupdError


class SetupdCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise SetupdServiceUnavailable(response)
        if response.status_code == 500:
            try:
                raise SetupdSetupError(response)
            except InvalidSetupdError:
                pass

        try:
            raise SetupdError(response)
        except InvalidSetupdError:
            RESTCommand.raise_from_response(response)
