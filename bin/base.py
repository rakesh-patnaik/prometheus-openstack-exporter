#!/usr/bin/env python
"""
OpenStack exporter for the prometheus monitoring system

Authors:
  Rakesh Patnaik<patsrakesh@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3,
as published by the Free Software Foundation.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranties of
MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re

class OSBase(object):
    FAIL = 0
    OK = 1
    UNKNOWN = 2

    def __init__(self, oscache, osclient):
        self.oscache = oscache
        self.osclient = osclient
        self.oscache.cache_me(self)
  
    def get_cache_data(self):
        return self.oscache.get_cache_data(self.get_cache_key())
        
    def build_cache_data(self):
        """ build a hash to store in cache """
        raise NotImplemented("Must be implemented by the subclass!")

    def get_cache_key(self):
        """ cache key """
        raise NotImplemented("Must be implemented by the subclass!")

    def get_stats(self):
        """ build stats for prometheus exporter """
        raise NotImplemented("Must be implemented by the subclass!")
    
    def gauge_name_sanitize(self, input):
        return re.sub(r'[^a-zA-Z0-9:_]', '_', input)
