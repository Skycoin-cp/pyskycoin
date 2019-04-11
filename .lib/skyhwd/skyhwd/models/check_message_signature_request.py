# coding: utf-8

"""
    Hardware Wallet Daemon API

    This is the hardware-wallet-daemon API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: steve@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CheckMessageSignatureRequest(object):
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
        'message': 'str',
        'signature': 'str',
        'address': 'str'
    }

    attribute_map = {
        'message': 'message',
        'signature': 'signature',
        'address': 'address'
    }

    def __init__(self, message=None, signature=None, address=None):  # noqa: E501
        """CheckMessageSignatureRequest - a model defined in OpenAPI"""  # noqa: E501

        self._message = None
        self._signature = None
        self._address = None
        self.discriminator = None

        self.message = message
        self.signature = signature
        self.address = address

    @property
    def message(self):
        """Gets the message of this CheckMessageSignatureRequest.  # noqa: E501


        :return: The message of this CheckMessageSignatureRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CheckMessageSignatureRequest.


        :param message: The message of this CheckMessageSignatureRequest.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def signature(self):
        """Gets the signature of this CheckMessageSignatureRequest.  # noqa: E501


        :return: The signature of this CheckMessageSignatureRequest.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this CheckMessageSignatureRequest.


        :param signature: The signature of this CheckMessageSignatureRequest.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def address(self):
        """Gets the address of this CheckMessageSignatureRequest.  # noqa: E501


        :return: The address of this CheckMessageSignatureRequest.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CheckMessageSignatureRequest.


        :param address: The address of this CheckMessageSignatureRequest.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

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
        if not isinstance(other, CheckMessageSignatureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
