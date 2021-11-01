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


class SequencingRunPrepKitInfo(object):
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
        'library_prep_kit_names': 'str',
        'num_samples': 'int',
        'lanes': 'list[LanePrepKitInfo]'
    }

    attribute_map = {
        'library_prep_kit_names': 'libraryPrepKitNames',
        'num_samples': 'numSamples',
        'lanes': 'lanes'
    }

    def __init__(self, library_prep_kit_names=None, num_samples=None, lanes=None, local_vars_configuration=None):  # noqa: E501
        """SequencingRunPrepKitInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._library_prep_kit_names = None
        self._num_samples = None
        self._lanes = None
        self.discriminator = None

        if library_prep_kit_names is not None:
            self.library_prep_kit_names = library_prep_kit_names
        if num_samples is not None:
            self.num_samples = num_samples
        if lanes is not None:
            self.lanes = lanes

    @property
    def library_prep_kit_names(self):
        """Gets the library_prep_kit_names of this SequencingRunPrepKitInfo.  # noqa: E501

        Names of LibraryPrepKits used (Names of custom kits are \"Custom\")  # noqa: E501

        :return: The library_prep_kit_names of this SequencingRunPrepKitInfo.  # noqa: E501
        :rtype: str
        """
        return self._library_prep_kit_names

    @library_prep_kit_names.setter
    def library_prep_kit_names(self, library_prep_kit_names):
        """Sets the library_prep_kit_names of this SequencingRunPrepKitInfo.

        Names of LibraryPrepKits used (Names of custom kits are \"Custom\")  # noqa: E501

        :param library_prep_kit_names: The library_prep_kit_names of this SequencingRunPrepKitInfo.  # noqa: E501
        :type: str
        """

        self._library_prep_kit_names = library_prep_kit_names

    @property
    def num_samples(self):
        """Gets the num_samples of this SequencingRunPrepKitInfo.  # noqa: E501

        Number of libraries  # noqa: E501

        :return: The num_samples of this SequencingRunPrepKitInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_samples

    @num_samples.setter
    def num_samples(self, num_samples):
        """Sets the num_samples of this SequencingRunPrepKitInfo.

        Number of libraries  # noqa: E501

        :param num_samples: The num_samples of this SequencingRunPrepKitInfo.  # noqa: E501
        :type: int
        """

        self._num_samples = num_samples

    @property
    def lanes(self):
        """Gets the lanes of this SequencingRunPrepKitInfo.  # noqa: E501

        Library prep kit and index adapter kit information for all lanes  # noqa: E501

        :return: The lanes of this SequencingRunPrepKitInfo.  # noqa: E501
        :rtype: list[LanePrepKitInfo]
        """
        return self._lanes

    @lanes.setter
    def lanes(self, lanes):
        """Sets the lanes of this SequencingRunPrepKitInfo.

        Library prep kit and index adapter kit information for all lanes  # noqa: E501

        :param lanes: The lanes of this SequencingRunPrepKitInfo.  # noqa: E501
        :type: list[LanePrepKitInfo]
        """

        self._lanes = lanes

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
        if not isinstance(other, SequencingRunPrepKitInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SequencingRunPrepKitInfo):
            return True

        return self.to_dict() != other.to_dict()
