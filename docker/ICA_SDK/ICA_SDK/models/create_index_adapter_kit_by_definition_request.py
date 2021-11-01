# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ICA_SDK.configuration import Configuration


class CreateIndexAdapterKitByDefinitionRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'definition_format': 'str',
        'definition': 'str',
        'skip_index_diversity_validation': 'bool'
    }

    attribute_map = {
        'definition_format': 'definitionFormat',
        'definition': 'definition',
        'skip_index_diversity_validation': 'skipIndexDiversityValidation'
    }

    def __init__(self, definition_format=None, definition=None, skip_index_diversity_validation=None, local_vars_configuration=None):  # noqa: E501
        """CreateIndexAdapterKitByDefinitionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._definition_format = None
        self._definition = None
        self._skip_index_diversity_validation = None
        self.discriminator = None

        self.definition_format = definition_format
        self.definition = definition
        if skip_index_diversity_validation is not None:
            self.skip_index_diversity_validation = skip_index_diversity_validation

    @property
    def definition_format(self):
        """Gets the definition_format of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501

        Definition format for the Definition. Supported value is yaml  # noqa: E501

        :return: The definition_format of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._definition_format

    @definition_format.setter
    def definition_format(self, definition_format):
        """Sets the definition_format of this CreateIndexAdapterKitByDefinitionRequest.

        Definition format for the Definition. Supported value is yaml  # noqa: E501

        :param definition_format: The definition_format of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and definition_format is None:  # noqa: E501
            raise ValueError("Invalid value for `definition_format`, must not be `None`")  # noqa: E501
        allowed_values = ["Yaml", "Tsv"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and definition_format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `definition_format` ({0}), must be one of {1}"  # noqa: E501
                .format(definition_format, allowed_values)
            )

        self._definition_format = definition_format

    @property
    def definition(self):
        """Gets the definition of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501

        Definition for the IndexAdapterKit  # noqa: E501

        :return: The definition of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this CreateIndexAdapterKitByDefinitionRequest.

        Definition for the IndexAdapterKit  # noqa: E501

        :param definition: The definition of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and definition is None:  # noqa: E501
            raise ValueError("Invalid value for `definition`, must not be `None`")  # noqa: E501

        self._definition = definition

    @property
    def skip_index_diversity_validation(self):
        """Gets the skip_index_diversity_validation of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501

        Flag to skip index diversity validation  # noqa: E501

        :return: The skip_index_diversity_validation of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_index_diversity_validation

    @skip_index_diversity_validation.setter
    def skip_index_diversity_validation(self, skip_index_diversity_validation):
        """Sets the skip_index_diversity_validation of this CreateIndexAdapterKitByDefinitionRequest.

        Flag to skip index diversity validation  # noqa: E501

        :param skip_index_diversity_validation: The skip_index_diversity_validation of this CreateIndexAdapterKitByDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._skip_index_diversity_validation = skip_index_diversity_validation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateIndexAdapterKitByDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateIndexAdapterKitByDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
