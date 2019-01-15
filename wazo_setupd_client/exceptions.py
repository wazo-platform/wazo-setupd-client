# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class SetupdError(HTTPError):

    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidSetupdError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
        except KeyError:
            raise InvalidSetupdError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(SetupdError, self).__init__(exception_message, response=response)


class SetupdServiceUnavailable(SetupdError):
    pass


class InvalidSetupdError(Exception):
    pass


class SetupdSetupError(SetupdError):
    pass
