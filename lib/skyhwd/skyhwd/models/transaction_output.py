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


class TransactionOutput(object):
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
        'address_index': 'int',
        'address': 'str',
        'coins': 'str',
        'hours': 'str'
    }

    attribute_map = {
        'address_index': 'address_index',
        'address': 'address',
        'coins': 'coins',
        'hours': 'hours'
    }

    def __init__(self, address_index=None, address=None, coins=None, hours=None):  # noqa: E501
        """TransactionOutput - a model defined in OpenAPI"""  # noqa: E501

        self._address_index = None
        self._address = None
        self._coins = None
        self._hours = None
        self.discriminator = None

        self.address_index = address_index
        self.address = address
        self.coins = coins
        self.hours = hours

    @property
    def address_index(self):
        """Gets the address_index of this TransactionOutput.  # noqa: E501


        :return: The address_index of this TransactionOutput.  # noqa: E501
        :rtype: int
        """
        return self._address_index

    @address_index.setter
    def address_index(self, address_index):
        """Sets the address_index of this TransactionOutput.


        :param address_index: The address_index of this TransactionOutput.  # noqa: E501
        :type: int
        """
        if address_index is None:
            raise ValueError("Invalid value for `address_index`, must not be `None`")  # noqa: E501

        self._address_index = address_index

    @property
    def address(self):
        """Gets the address of this TransactionOutput.  # noqa: E501


        :return: The address of this TransactionOutput.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this TransactionOutput.


        :param address: The address of this TransactionOutput.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def coins(self):
        """Gets the coins of this TransactionOutput.  # noqa: E501


        :return: The coins of this TransactionOutput.  # noqa: E501
        :rtype: str
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this TransactionOutput.


        :param coins: The coins of this TransactionOutput.  # noqa: E501
        :type: str
        """
        if coins is None:
            raise ValueError("Invalid value for `coins`, must not be `None`")  # noqa: E501

        self._coins = coins

    @property
    def hours(self):
        """Gets the hours of this TransactionOutput.  # noqa: E501


        :return: The hours of this TransactionOutput.  # noqa: E501
        :rtype: str
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Sets the hours of this TransactionOutput.


        :param hours: The hours of this TransactionOutput.  # noqa: E501
        :type: str
        """
        if hours is None:
            raise ValueError("Invalid value for `hours`, must not be `None`")  # noqa: E501

        self._hours = hours

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
        if not isinstance(other, TransactionOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
