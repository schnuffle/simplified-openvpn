#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=R0904

"""File that contains SimplifiedOpenvpnSuggest class."""

import os
import json
from simplified_openvpn_helper import SimplifiedOpenvpnHelper as _helper

class SimplifiedOpenvpnSuggest:
    """Class that contains methods that will give you suggestions."""
    @staticmethod
    def get_value_from_sample(key):
        """Get suggestion from sample config."""
        sample_path = os.path.dirname(os.path.realpath(__file__)) + '/sovpn.json'
        sample = _helper.read_file_as_value(sample_path)
        defaults = json.loads(sample)
        return defaults['server'][key]

    @staticmethod
    def hostname():
        """Returns suggestion for hostname"""
        suggestion = SimplifiedOpenvpnSuggest.get_value_from_sample(_helper.current_method())
        if suggestion is None:
            suggestion = _helper.fetch_hostname_by_system()
        if suggestion is None:
            suggestion = _helper.fetch_hostname_by_reverse_dns()
        return suggestion

    @staticmethod
    def protocol():
        """Getting suggestion for protocol."""
        suggestion = SimplifiedOpenvpnSuggest.get_value_from_sample(_helper.current_method())
        return suggestion