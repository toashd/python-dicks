#!/usr/bin/env python

class DicksError(Exception):
    '''Base class for Dicks errors'''

    @property
    def message(self):
        '''Returns the first argument used to construct this error.'''
        return self.args[0]

