# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ICA_SDK
from ICA_SDK.api.planned_runs_api import PlannedRunsApi  # noqa: E501
from ICA_SDK.rest import ApiException


class TestPlannedRunsApi(unittest.TestCase):
    """PlannedRunsApi unit test stubs"""

    def setUp(self):
        self.api = ICA_SDK.api.planned_runs_api.PlannedRunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_planned_run(self):
        """Test case for create_planned_run

        Create sequencing run plan.  # noqa: E501
        """
        pass

    def test_import_planned_run(self):
        """Test case for import_planned_run

        Import a planned run from sample sheet.  # noqa: E501
        """
        pass

    def test_lock_planned_run(self):
        """Test case for lock_planned_run

        Lock a planned run.  # noqa: E501
        """
        pass

    def test_replace_planned_run(self):
        """Test case for replace_planned_run

        Replace planned run configuration, contents, and analysis configurations.  # noqa: E501
        """
        pass

    def test_start_planned_run(self):
        """Test case for start_planned_run

        Start a planned sequencing run.  # noqa: E501
        """
        pass

    def test_unlock_planned_run(self):
        """Test case for unlock_planned_run

        Unlock a planned run.  # noqa: E501
        """
        pass

    def test_update_planned_run_config(self):
        """Test case for update_planned_run_config

        Update planned run configuration.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
