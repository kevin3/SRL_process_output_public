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
from ICA_SDK.models.folder_response import FolderResponse  # noqa: E501
from ICA_SDK.rest import ApiException

class TestFolderResponse(unittest.TestCase):
    """FolderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FolderResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ICA_SDK.models.folder_response.FolderResponse()  # noqa: E501
        if include_optional :
            return FolderResponse(
                id = '0', 
                name = '0', 
                volume_id = '0', 
                parent_folder_id = '0', 
                volume_name = '0', 
                tenant_id = '0', 
                sub_tenant_id = '0', 
                urn = '0', 
                path = '0', 
                acl = [
                    '0'
                    ], 
                inherited_acl = [
                    '0'
                    ], 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by = '0', 
                metadata = ICA_SDK.models.metadata.metadata(), 
                volume_metadata = ICA_SDK.models.volume_metadata.volumeMetadata(), 
                job_status = 'None', 
                job_id = '0', 
                archive_job_storage_tier = 'None'
            )
        else :
            return FolderResponse(
        )

    def testFolderResponse(self):
        """Test FolderResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
