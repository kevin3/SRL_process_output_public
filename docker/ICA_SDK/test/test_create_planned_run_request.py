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
from ICA_SDK.models.create_planned_run_request import CreatePlannedRunRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestCreatePlannedRunRequest(unittest.TestCase):
    """CreatePlannedRunRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreatePlannedRunRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.create_planned_run_request.CreatePlannedRunRequest()  # noqa: E501
        if include_optional :
            return CreatePlannedRunRequest(
                run_configuration = ICA_SDK.models.create_sequencing_run_configuration_request.CreateSequencingRunConfigurationRequest(
                    instrument_type = '0', 
                    instrument_platform = '0', 
                    run_name = '0', 
                    description = '0', 
                    regulatory_mode = 'RUO', 
                    num_cycles_read1 = 0, 
                    num_cycles_read2 = 0, 
                    read_type = 'Single', 
                    num_cycles_index1 = 0, 
                    num_cycles_index2 = 0, 
                    use_custom_primer_for_read1 = True, 
                    use_custom_primer_for_read2 = True, 
                    use_custom_primer_for_index1 = True, 
                    use_custom_primer_for_index2 = True, 
                    input_container_identifier = '0', ), 
                run_contents = ICA_SDK.models.update_sequencing_run_contents_request.UpdateSequencingRunContentsRequest(
                    allow_index_updates = True, 
                    lane_contents = [
                        ICA_SDK.models.lane_content.LaneContent(
                            lane_number = 56, 
                            same_as_lane_number = 56, 
                            adapter_sequence_read1 = '0', 
                            adapter_sequence_read2 = '0', 
                            lane_libraries = [
                                ICA_SDK.models.lane_library.LaneLibrary(
                                    sample_name = '0', 
                                    sample_urn = '0', 
                                    project_name = '0', 
                                    library_name = '0', 
                                    library_urn = '0', 
                                    adapter_sequence_read1 = '0', 
                                    adapter_sequence_read2 = '0', 
                                    index1_sequence = '0', 
                                    index2_sequence = '0', 
                                    index_container_position = '0', 
                                    index1_name = '0', 
                                    index2_name = '0', 
                                    library_prep_kit_urn = '0', 
                                    index_adapter_kit_urn = '0', )
                                ], )
                        ], ), 
                run_analysis_configurations = [
                    ICA_SDK.models.create_sequencing_run_analysis_configuration_request.CreateSequencingRunAnalysisConfigurationRequest(
                        name = '0', 
                        description = '0', 
                        analysis_version_definition_id = '0', 
                        settings = ICA_SDK.models.settings.settings(), 
                        sample_settings = [
                            ICA_SDK.models.sample_setting_entry.SampleSettingEntry(
                                sample_id = '0', 
                                settings = ICA_SDK.models.settings.settings(), )
                            ], )
                    ], 
                is_favorite = True, 
                acl = [
                    '0'
                    ]
            )
        else :
            return CreatePlannedRunRequest(
                run_configuration = ICA_SDK.models.create_sequencing_run_configuration_request.CreateSequencingRunConfigurationRequest(
                    instrument_type = '0', 
                    instrument_platform = '0', 
                    run_name = '0', 
                    description = '0', 
                    regulatory_mode = 'RUO', 
                    num_cycles_read1 = 0, 
                    num_cycles_read2 = 0, 
                    read_type = 'Single', 
                    num_cycles_index1 = 0, 
                    num_cycles_index2 = 0, 
                    use_custom_primer_for_read1 = True, 
                    use_custom_primer_for_read2 = True, 
                    use_custom_primer_for_index1 = True, 
                    use_custom_primer_for_index2 = True, 
                    input_container_identifier = '0', ),
        )

    def testCreatePlannedRunRequest(self):
        """Test CreatePlannedRunRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
