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
from ICA_SDK.models.index_adapter_kit_compact import IndexAdapterKitCompact  # noqa: E501
from ICA_SDK.rest import ApiException

class TestIndexAdapterKitCompact(unittest.TestCase):
    """IndexAdapterKitCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IndexAdapterKitCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.index_adapter_kit_compact.IndexAdapterKitCompact()  # noqa: E501
        if include_optional :
            return IndexAdapterKitCompact(
                id = '0', 
                urn = '0', 
                href = '0', 
                name = '0', 
                display_name = '0', 
                organization = '0', 
                is_illumina = True, 
                description = '0', 
                allowed_index_strategies = [
                    '0'
                    ], 
                adapter_sequence_read1 = '0', 
                adapter_sequence_read2 = '0', 
                settings = ICA_SDK.models.index_adapter_kit_settings_response.IndexAdapterKitSettingsResponse(
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
                        }, ), 
                checksum = '0', 
                sub_tenant_id = '0', 
                acl = [
                    '0'
                    ], 
                tenant_id = '0', 
                tenant_name = '0', 
                created_by_client_id = '0', 
                created_by = '0', 
                modified_by = '0', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return IndexAdapterKitCompact(
        )

    def testIndexAdapterKitCompact(self):
        """Test IndexAdapterKitCompact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
