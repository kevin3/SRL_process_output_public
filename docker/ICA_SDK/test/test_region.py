# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ICA_SDK
from ICA_SDK.models.region import Region  # noqa: E501
from ICA_SDK.rest import ApiException

class TestRegion(unittest.TestCase):
    """Region unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Region
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.region.Region()  # noqa: E501
        if include_optional :
            return Region(
                name = '0', 
                display_name = '0', 
                base_url = '0', 
                is_enabled = True
            )
        else :
            return Region(
        )

    def testRegion(self):
        """Test Region"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
