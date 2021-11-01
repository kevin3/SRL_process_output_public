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
from ICA_SDK.models.update_library_prep_kit_request import UpdateLibraryPrepKitRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestUpdateLibraryPrepKitRequest(unittest.TestCase):
    """UpdateLibraryPrepKitRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateLibraryPrepKitRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.update_library_prep_kit_request.UpdateLibraryPrepKitRequest()  # noqa: E501
        if include_optional :
            return UpdateLibraryPrepKitRequest(
                name = '0', 
                display_name = '0', 
                organization = '0', 
                description = '0', 
                allowed_read_types = [
                    'Single'
                    ], 
                default_read1_length = 0, 
                default_read2_length = 0, 
                settings = ICA_SDK.models.library_prep_kit_settings.LibraryPrepKitSettings(
                    default_read_type = 'Single', ), 
                checksum = '0', 
                is_application_specific = True, 
                index_adapter_kit_ids = [
                    '0'
                    ], 
                force = True, 
                acl = [
                    '0'
                    ]
            )
        else :
            return UpdateLibraryPrepKitRequest(
        )

    def testUpdateLibraryPrepKitRequest(self):
        """Test UpdateLibraryPrepKitRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
