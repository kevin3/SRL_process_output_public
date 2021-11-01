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
from ICA_SDK.models.instrument_platform_info import InstrumentPlatformInfo  # noqa: E501
from ICA_SDK.rest import ApiException

class TestInstrumentPlatformInfo(unittest.TestCase):
    """InstrumentPlatformInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstrumentPlatformInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.instrument_platform_info.InstrumentPlatformInfo()  # noqa: E501
        if include_optional :
            return InstrumentPlatformInfo(
                instrument_platform = '0', 
                display_name = '0', 
                run_planning_supported = True, 
                cloud_orchestration_supported = True, 
                require_instrument_type = True, 
                max_number_of_lanes = 56, 
                supported_analysis_locations = [
                    '0'
                    ], 
                configure_flowcell_type = True, 
                flow_cell_types = [
                    ICA_SDK.models.flow_cell_type.FlowCellType(
                        type = '0', 
                        max_number_of_lanes = 56, )
                    ], 
                read1_length_min = 56, 
                read1_length_max = 56, 
                read2_length_min = 56, 
                read2_length_max = 56, 
                multi_analysis_configuration = ICA_SDK.models.multi_analysis_configuration.MultiAnalysisConfiguration(
                    max_cloud_analyses = 56, 
                    max_cloud_total_physical_configurations = 56, 
                    max_cloud_total_logical_configurations = 56, 
                    max_cloud_logical_configurations_per_physical = 56, 
                    max_local_analyses = 56, 
                    max_local_total_physical_configurations = 56, 
                    max_local_total_logical_configurations = 56, 
                    max_local_logical_configurations_per_physical = 56, )
            )
        else :
            return InstrumentPlatformInfo(
        )

    def testInstrumentPlatformInfo(self):
        """Test InstrumentPlatformInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
