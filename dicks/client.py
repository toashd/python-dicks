#!/usr/bin/env python

'''A library that provides a Python interface to the Dicks API'''

import requests
import json as simplejson

from dicks import DicksError

class Client(object):

    def __init__(self, base_url=None):
        if base_url is None:
            self.base_url = 'https://dicks-api.herokuapp.com/'
        else:
            self.base_url = base_url

    def get_dicks(self, amount = 5, size = None):
        '''Returns a list of dicks.

        Args:
          amount:
            The numeric amount of dicks
          size:
            The string size of dicks
          Returns:
            A list full of dicks
        '''

        if amount >= 9000:
            raise DicksError("Over 9000 dicks currently not supported\nReason: Too many dicks.")

        params = {}

        if size:
            params['size'] = size

        url  = '%s/dicks/%i' % (self.base_url, amount)
        json = self._request_url(url, 'GET', data=params)

        return simplejson.loads(json.text)['dicks']

    def get_dicks_served(self):
        '''Returns the number of dicks served.

          Returns:
            The numeric value of dicks served.
        '''

        url  = '%s/dicks_served_counter' % (self.base_url)
        json = self._request_url(url, 'GET')

        return simplejson.loads(json.text)['dick_count']

    def _request_url(self, url, verb, data=None):
        try:
            return requests.get(
                url,
                params=data,
                verify=True
                )
        except requests.RequestException as e:
            raise DicksError(str(e))

