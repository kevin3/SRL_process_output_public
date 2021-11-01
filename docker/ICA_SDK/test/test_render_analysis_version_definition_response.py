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
from ICA_SDK.models.render_analysis_version_definition_response import RenderAnalysisVersionDefinitionResponse  # noqa: E501
from ICA_SDK.rest import ApiException

class TestRenderAnalysisVersionDefinitionResponse(unittest.TestCase):
    """RenderAnalysisVersionDefinitionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RenderAnalysisVersionDefinitionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.render_analysis_version_definition_response.RenderAnalysisVersionDefinitionResponse()  # noqa: E501
        if include_optional :
            return RenderAnalysisVersionDefinitionResponse(
                validation_errors = [
                    ICA_SDK.models.render_message.RenderMessage(
                        field_id = '0', 
                        sample_id = '0', 
                        message = '0', )
                    ], 
                validation_warnings = [
                    ICA_SDK.models.render_message.RenderMessage(
                        field_id = '0', 
                        sample_id = '0', 
                        message = '0', )
                    ], 
                analysis_version_definition = ICA_SDK.models.analysis_version_definition_compact.AnalysisVersionDefinitionCompact(
                    id = '0', 
                    urn = '0', 
                    href = '0', 
                    version = '0', 
                    description = '0', 
                    supported_instrument_platform_and_types = [
                        ICA_SDK.models.instrument_platform_and_types_response.InstrumentPlatformAndTypesResponse(
                            instrument_platform = '0', 
                            instrument_types = [
                                '0'
                                ], )
                        ], 
                    status = '0', 
                    analysis_type = '0', 
                    is_dragen = True, 
                    analysis_settings = ICA_SDK.models.analysis_settings.analysisSettings(), 
                    settings = ICA_SDK.models.analysis_version_definition_settings.AnalysisVersionDefinitionSettings(
                        sample_sheet = ICA_SDK.models.analysis_version_definition_settings_sample_sheet_configuration.AnalysisVersionDefinitionSettingsSampleSheetConfiguration(
                            bcl_convert_section_settings = {
                                'key' : '0'
                                }, 
                            analysis_section_settings = {
                                'key' : '0'
                                }, 
                            cloud_section_settings = {
                                'key' : '0'
                                }, ), 
                        run_analysis_settings = ICA_SDK.models.run_analysis_settings.runAnalysisSettings(), 
                        run_setup_validation = ICA_SDK.models.run_setup_validation.RunSetupValidation(
                            require_unique_sample_ids_per_lane = True, 
                            enable_custom_prep_kits = True, 
                            read1_length_min = 56, 
                            read1_length_max = 56, 
                            read2_length_min = 56, 
                            read2_length_max = 56, 
                            allowed_index_strategies = [
                                'NoIndex'
                                ], 
                            allowed_read_types = [
                                'Single'
                                ], 
                            allow_deviations = True, 
                            deviation_warning_message = '0', 
                            custom_prep_kit_warning_message = '0', 
                            skip_validate_index_cycles_with_index_sequence_lengths = True, ), 
                        workflow_metadata = ICA_SDK.models.workflow_metadata_dto.WorkflowMetadataDto(
                            workflow_type = '0', 
                            workflow_url = '0', 
                            volume_size_in_gigabytes = 56, 
                            tags = ICA_SDK.models.tags.tags(), 
                            workflow_params = ICA_SDK.models.workflow_params.workflowParams(), 
                            workflow_resources_folder = '0', ), ), 
                    skip_analysis_section = True, 
                    analysis_sample_settings = ICA_SDK.models.analysis_sample_settings.analysisSampleSettings(), 
                    on_render_require_run_contents = True, 
                    analysis_definition = ICA_SDK.models.analysis_definition_compact.AnalysisDefinitionCompact(
                        id = '0', 
                        urn = '0', 
                        href = '0', 
                        name = '0', 
                        organization = '0', 
                        is_illumina = True, 
                        description = '0', 
                        status = '0', 
                        illumina_kit_support_mode = '0', 
                        regulatory_mode = '0', 
                        display_name = '0', 
                        analysis_versions = ICA_SDK.models.analysis_version_definition_compact_item_list.AnalysisVersionDefinitionCompactItemList(
                            href_items = '0', 
                            items = [
                                ICA_SDK.models.analysis_version_definition_compact.AnalysisVersionDefinitionCompact(
                                    id = '0', 
                                    urn = '0', 
                                    href = '0', 
                                    version = '0', 
                                    description = '0', 
                                    status = '0', 
                                    analysis_type = '0', 
                                    is_dragen = True, 
                                    analysis_settings = ICA_SDK.models.analysis_settings.analysisSettings(), 
                                    skip_analysis_section = True, 
                                    analysis_sample_settings = ICA_SDK.models.analysis_sample_settings.analysisSampleSettings(), 
                                    on_render_require_run_contents = True, 
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
                                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            item_count = 56, ), 
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
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
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
                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                run_analysis_configuration = ICA_SDK.models.create_sequencing_run_analysis_configuration_request.CreateSequencingRunAnalysisConfigurationRequest(
                    name = '0', 
                    description = '0', 
                    analysis_version_definition_id = '0', 
                    settings = ICA_SDK.models.settings.settings(), 
                    sample_settings = [
                        ICA_SDK.models.sample_setting_entry.SampleSettingEntry(
                            sample_id = '0', 
                            settings = ICA_SDK.models.settings.settings(), )
                        ], ), 
                changed_setting_ids = [
                    '0'
                    ], 
                changed_setting_value_ids = [
                    '0'
                    ], 
                changed_sample_setting_ids = [
                    '0'
                    ], 
                changed_sample_setting_value_ids = None
            )
        else :
            return RenderAnalysisVersionDefinitionResponse(
        )

    def testRenderAnalysisVersionDefinitionResponse(self):
        """Test RenderAnalysisVersionDefinitionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
