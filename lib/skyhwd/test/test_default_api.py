# coding: utf-8

"""
    Hardware Wallet Daemon API

    This is the hardware-wallet-daemon API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: steve@skycoin.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import skyhwd
from skyhwd.api.default_api import DefaultApi  # noqa: E501
from skyhwd.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = skyhwd.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_apply_settings_post(self):
        """Test case for apply_settings_post

        """
        pass

    def test_backup_post(self):
        """Test case for backup_post

        """
        pass

    def test_cancel_put(self):
        """Test case for cancel_put

        """
        pass

    def test_check_message_signature_post(self):
        """Test case for check_message_signature_post

        """
        pass

    def test_connected_get(self):
        """Test case for connected_get

        """
        pass

    def test_csrf_get(self):
        """Test case for csrf_get

        """
        pass

    def test_features_get(self):
        """Test case for features_get

        """
        pass

    def test_firmware_update_put(self):
        """Test case for firmware_update_put

        """
        pass

    def test_generate_addresses_post(self):
        """Test case for generate_addresses_post

        """
        pass

    def test_generate_mnemonic_post(self):
        """Test case for generate_mnemonic_post

        """
        pass

    def test_intermediate_passphrase_post(self):
        """Test case for intermediate_passphrase_post

        """
        pass

    def test_intermediate_pin_matrix_post(self):
        """Test case for intermediate_pin_matrix_post

        """
        pass

    def test_intermediate_word_post(self):
        """Test case for intermediate_word_post

        """
        pass

    def test_recovery_post(self):
        """Test case for recovery_post

        """
        pass

    def test_set_mnemonic_post(self):
        """Test case for set_mnemonic_post

        """
        pass

    def test_set_pin_code_post(self):
        """Test case for set_pin_code_post

        """
        pass

    def test_sign_message_post(self):
        """Test case for sign_message_post

        """
        pass

    def test_transaction_sign_post(self):
        """Test case for transaction_sign_post

        """
        pass

    def test_wipe_delete(self):
        """Test case for wipe_delete

        """
        pass


if __name__ == '__main__':
    unittest.main()
