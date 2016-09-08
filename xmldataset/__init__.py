""" Extracts XML into Python Datasets based upon a simple text
 profile markup language """

# -*- coding: utf-8 -*-
#  pylint: disable=line-too-long

__author__ = 'James Spurin'
__email__ = 'james@spurin.com'
__version__ = '0.1.7'

from ._XMLDataset import _XMLDataset
from .parsing import parse_using_profile
