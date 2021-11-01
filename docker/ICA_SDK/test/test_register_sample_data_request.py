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
from ICA_SDK.models.register_sample_data_request import RegisterSampleDataRequest  # noqa: E501
from ICA_SDK.rest import ApiException

class TestRegisterSampleDataRequest(unittest.TestCase):
    """RegisterSampleDataRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegisterSampleDataRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.register_sample_data_request.RegisterSampleDataRequest()  # noqa: E501
        if include_optional :
            return RegisterSampleDataRequest(
                skip_copy_files_to_project_volume = True, 
                total_sample_count = 56, 
                total_dataset_count = 56, 
                sample_id = '0', 
                sample_name = '0', 
                project_name = '0', 
                external_sample_id = '0', 
                external_project_id = '0', 
                external_analysis_run_id = '0', 
                analysis_datasets = [
                    ICA_SDK.models.create_analysis_dataset_parameters.CreateAnalysisDatasetParameters(
                        name = '0', 
                        display_name = '0', 
                        external_id = '0', 
                        task_run_id = '0', 
                        workflow_run_id = '0', 
                        lane_number = 1, 
                        data_folder_urn = '0', 
                        data_folder_volume_path = '0', 
                        attributes = ICA_SDK.models.attributes.attributes(), 
                        type = '0', 
                        qc_status = '0', 
                        qc_status_summary = '0', 
                        file_urns = [
                            '0'
                            ], )
                    ]
            )
        else :
            return RegisterSampleDataRequest(
        )

    def testRegisterSampleDataRequest(self):
        """Test RegisterSampleDataRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
