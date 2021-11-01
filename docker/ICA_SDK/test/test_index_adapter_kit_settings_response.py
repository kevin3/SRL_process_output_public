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
from ICA_SDK.models.index_adapter_kit_settings_response import IndexAdapterKitSettingsResponse  # noqa: E501
from ICA_SDK.rest import ApiException

class TestIndexAdapterKitSettingsResponse(unittest.TestCase):
    """IndexAdapterKitSettingsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IndexAdapterKitSettingsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.index_adapter_kit_settings_response.IndexAdapterKitSettingsResponse()  # noqa: E501
        if include_optional :
            return IndexAdapterKitSettingsResponse(
                default_index_strategy = '0', 
                override_cycles = '0', 
                fixed_layout = True, 
                multiplate = True, 
                multiple_indexes_per_well = True, 
                fixed_index_positions = [
                    '0'
                    ], 
                enable_custom_index_cycles = True, 
                num_cycles_index1_override = 56, 
                num_cycles_index2_override = 56, 
                fixed_layout_position_key_by_index_id = True, 
                custom_bcl_convert_settings = {
                    'key' : '0'
                    }
            )
        else :
            return IndexAdapterKitSettingsResponse(
        )

    def testIndexAdapterKitSettingsResponse(self):
        """Test IndexAdapterKitSettingsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
