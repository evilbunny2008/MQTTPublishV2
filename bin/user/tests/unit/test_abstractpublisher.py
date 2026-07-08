#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring
# pylint: disable=invalid-name
import unittest
import mock

import helpers

import configobj
import random

import paho.mqtt

import user.MQTTPublishV2
import mqttstubs

class TestAbstractPublisher(unittest.TestCase):
    def test_get_publisher_for_paho_mqtt_v1(self):
        mock_logger = mock.Mock()
        mock_publisher = mock.Mock()

        config_dict = {}
        config = configobj.ConfigObj(config_dict)

        with mock.patch('user.MQTTPublishV2.PublisherV1') as mock_client:
            with mqttstubs.patch_delattr(user.MQTTPublishV2.mqtt, 'CallbackAPIVersion'):
                user.MQTTPublishV2.AbstractPublisher.get_publisher(mock_logger, mock_publisher, config)

                mock_client.assert_called_once_with(mock_logger, mock_publisher, config)

    def test_get_publisher_for_paho_mqtt_v2(self):
        mock_logger = mock.Mock()
        mock_publisher = mock.Mock()

        protocol_string = 'MQTTv5'

        config_dict = {
            'protocol': getattr(paho.mqtt.client, protocol_string, 0),
        }
        config = configobj.ConfigObj(config_dict)

        with mock.patch('user.MQTTPublishV2.PublisherV2') as mock_client:
            with mqttstubs.patch_addattr(user.MQTTPublishV2.mqtt, 'CallbackAPIVersion'):
                user.MQTTPublishV2.AbstractPublisher.get_publisher(mock_logger, mock_publisher, config)

                mock_client.assert_called_once_with(mock_logger, mock_publisher, config)

    def test_get_publisher_for_paho_mqtt_v2_mqtt_v3(self):
        mock_logger = mock.Mock()
        mock_publisher = mock.Mock()

        protocol_string = random.choice(['MQTTv31', 'MQTTv311'])

        config_dict = {
            'protocol': getattr(paho.mqtt.client, protocol_string, 0),
        }
        config = configobj.ConfigObj(config_dict)

        with mock.patch('user.MQTTPublishV2.PublisherV2MQTT3') as mock_client:
            with mqttstubs.patch_addattr(user.MQTTPublishV2.mqtt, 'CallbackAPIVersion'):
                user.MQTTPublishV2.AbstractPublisher.get_publisher(mock_logger, mock_publisher, config)

                mock_client.assert_called_once_with(mock_logger, mock_publisher, config)

if __name__ == '__main__':
    helpers.run_tests()
