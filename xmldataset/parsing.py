# -*- coding: utf-8 -*-

"""
xmldataset.parsing
~~~~~~~~~~~~~~~~~~

This module contains the different parsing functions.
"""

# ------------------------------------------------------------------------------
#   Attempt to use cElementTree, otherwise fall back on ElementTree
# ------------------------------------------------------------------------------
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


from ._XMLDataset import _XMLDataset


def parse_using_profile(xml, profile, **options):
    """Parses XML based upon the profile"""

    # ------------------------------------------------------------------------------
    #    Create an object, passing the options to the object
    # ------------------------------------------------------------------------------
    obj = _XMLDataset(options)

    # ------------------------------------------------------------------------------
    #    Convert the source input profile to a python structure
    # ------------------------------------------------------------------------------
    obj._profile = obj._expand_profile(profile)

    # ------------------------------------------------------------------------------
    #    Capture an ElementTree.Element from an XML String ( Equivalent to
    #    getroot() on parse file )
    # ------------------------------------------------------------------------------
    xml_root = ET.fromstring(xml)

    # ------------------------------------------------------------------------------
    #    Process XML Data
    # ------------------------------------------------------------------------------
    obj._process_data(xml_root)

    # ------------------------------------------------------------------------------
    #    If the object has dispatch parameters, flush any remaining records
    # ------------------------------------------------------------------------------
    if hasattr(obj,'dispatch'):
        obj._dispatch_all()

    else:
        # ------------------------------------------------------------------------------
        #    Otherwise return the data structure
        # ------------------------------------------------------------------------------
        return obj.data_structure
