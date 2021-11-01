# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ICA_SDK.api_client import ApiClient
from ICA_SDK.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlannedRunsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_planned_run(self, **kwargs):  # noqa: E501
        """Create sequencing run plan.  # noqa: E501

        Create sequencing run plan, with configuration required for an instrument to start the run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_planned_run(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePlannedRunRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SequencingRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_planned_run_with_http_info(**kwargs)  # noqa: E501

    def create_planned_run_with_http_info(self, **kwargs):  # noqa: E501
        """Create sequencing run plan.  # noqa: E501

        Create sequencing run plan, with configuration required for an instrument to start the run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_planned_run_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePlannedRunRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SequencingRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_planned_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs:plan', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SequencingRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_planned_run(self, **kwargs):  # noqa: E501
        """Import a planned run from sample sheet.  # noqa: E501

        Import a planned run based on sample sheet, return information of the import result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_planned_run(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ImportPlannedRunRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ImportPlannedRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.import_planned_run_with_http_info(**kwargs)  # noqa: E501

    def import_planned_run_with_http_info(self, **kwargs):  # noqa: E501
        """Import a planned run from sample sheet.  # noqa: E501

        Import a planned run based on sample sheet, return information of the import result.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_planned_run_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param ImportPlannedRunRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ImportPlannedRunResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_planned_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs:import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImportPlannedRunResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lock_planned_run(self, run_id, **kwargs):  # noqa: E501
        """Lock a planned run.  # noqa: E501

        Lock the planned run associated with a given sequencing run ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lock_planned_run(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SequencingRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.lock_planned_run_with_http_info(run_id, **kwargs)  # noqa: E501

    def lock_planned_run_with_http_info(self, run_id, **kwargs):  # noqa: E501
        """Lock a planned run.  # noqa: E501

        Lock the planned run associated with a given sequencing run ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lock_planned_run_with_http_info(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SequencingRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lock_planned_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'run_id' is set
        if self.api_client.client_side_validation and ('run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `run_id` when calling `lock_planned_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs/{runId}:lock', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SequencingRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_planned_run(self, run_id, **kwargs):  # noqa: E501
        """Replace planned run configuration, contents, and analysis configurations.  # noqa: E501

        For a given sequencing run ID, replace the existing planned run with user input. This may include run configuration, run contents, and analysis configurations. Only applicable to runs in planning stage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_planned_run(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param ReplacePlannedRunRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SequencingRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.replace_planned_run_with_http_info(run_id, **kwargs)  # noqa: E501

    def replace_planned_run_with_http_info(self, run_id, **kwargs):  # noqa: E501
        """Replace planned run configuration, contents, and analysis configurations.  # noqa: E501

        For a given sequencing run ID, replace the existing planned run with user input. This may include run configuration, run contents, and analysis configurations. Only applicable to runs in planning stage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_planned_run_with_http_info(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param ReplacePlannedRunRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SequencingRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'run_id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_planned_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'run_id' is set
        if self.api_client.client_side_validation and ('run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `run_id` when calling `replace_planned_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs/{runId}/plan', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SequencingRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_planned_run(self, run_id, **kwargs):  # noqa: E501
        """Start a planned sequencing run.  # noqa: E501

        Start a planned sequencing run, and return information about that run. Only applicable to planned runs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_planned_run(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param StartPlannedRunRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SequencingRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.start_planned_run_with_http_info(run_id, **kwargs)  # noqa: E501

    def start_planned_run_with_http_info(self, run_id, **kwargs):  # noqa: E501
        """Start a planned sequencing run.  # noqa: E501

        Start a planned sequencing run, and return information about that run. Only applicable to planned runs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_planned_run_with_http_info(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param StartPlannedRunRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SequencingRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'run_id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_planned_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'run_id' is set
        if self.api_client.client_side_validation and ('run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `run_id` when calling `start_planned_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs/{runId}:start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SequencingRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unlock_planned_run(self, run_id, **kwargs):  # noqa: E501
        """Unlock a planned run.  # noqa: E501

        For a given sequencing run ID, unlock the planned run for the current request token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unlock_planned_run(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SequencingRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.unlock_planned_run_with_http_info(run_id, **kwargs)  # noqa: E501

    def unlock_planned_run_with_http_info(self, run_id, **kwargs):  # noqa: E501
        """Unlock a planned run.  # noqa: E501

        For a given sequencing run ID, unlock the planned run for the current request token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unlock_planned_run_with_http_info(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SequencingRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'run_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unlock_planned_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'run_id' is set
        if self.api_client.client_side_validation and ('run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `run_id` when calling `unlock_planned_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs/{runId}:unlock', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SequencingRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_planned_run_config(self, run_id, **kwargs):  # noqa: E501
        """Update planned run configuration.  # noqa: E501

        For a given sequencing run ID, update the planned run configuration. Only applicable to runs in planning stage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_planned_run_config(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param UpdateSequencingRunConfigurationRequest body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SequencingRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_planned_run_config_with_http_info(run_id, **kwargs)  # noqa: E501

    def update_planned_run_config_with_http_info(self, run_id, **kwargs):  # noqa: E501
        """Update planned run configuration.  # noqa: E501

        For a given sequencing run ID, update the planned run configuration. Only applicable to runs in planning stage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_planned_run_config_with_http_info(run_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str run_id: (required)
        :param UpdateSequencingRunConfigurationRequest body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SequencingRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'run_id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_planned_run_config" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'run_id' is set
        if self.api_client.client_side_validation and ('run_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['run_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `run_id` when calling `update_planned_run_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'run_id' in local_var_params:
            path_params['runId'] = local_var_params['run_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sequencing/runs/{runId}/config', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SequencingRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
