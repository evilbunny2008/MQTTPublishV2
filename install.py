#    Copyright (c) 2025 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

""" Installer for MQTTPublishV2 service.

To uninstall run
weectl extension uninstall MQTTPublishV2
"""

from io import StringIO

import configobj

from weecfg.extension import ExtensionInstaller

VERSION = "2.0.8"

CONFIG = """
[MQTTPublishV2]
    # Whether the service is enabled or not.
    # Valid values: true or false
    # Default is true.
    enable = false

    # Controls the MQTT logging.
    # Default is false.
    log_mqtt = false

    # The maximum number of times to try to reconnect.
    # Default is 5.
    max_retries = 5

    # The clientid to connect with.
    # Default is MQTTPublish-xxxx.
    #    Where xxxx is a random number between 1000 and 9999.
    clientid =

    # The MQTT server.
    # Default is localhost.
    host = localhost

    # Maximum period in seconds allowed between communications with the broker.
    # Default is 60.
    keepalive = 60

    # The port to connect to.
    # Default is 1883.
    port = 1883

    # The MQTT protocol to use
    # Valid values: MQTTv31, MQTTv311, MQTTv5
    # Default is MQTTv311,
    protocol = MQTTv5

    # username for broker authentication.
    # Default is None.
    username = None

    # password for broker authentication.
    # Default is None.
    password = None

    # The TLS options that are passed to tls_set method of the MQTT client.
    # For additional information see, https://eclipse.org/paho/clients/python/docs/strptime-format-codes
    [[tls]]
        # Turn tls on and off.
        # Default is true.
        enable = false

        # Path to the Certificate Authority certificate files that are to be treated as trusted by this client.
        ca_certs = /etc/ssl/certs/ca-certificates.crt

        # The PEM encoded client certificate and private keys.
        # Default is None
        # certfile = None

        # The certificate requirements that the client imposes on the broker.
        # Valid values: none, optional, required
        # Default is required,
        certs_required = required

        # The encryption ciphers that are allowable for this connection. Specify None to use the defaults
        # Default is None.
        # ciphers = None

        # The private keys.
        # Default is None
        # keyfile = None

        # The version of the SSL/TLS protocol to be used.
        # Valid values: sslv2, sslv23, sslv3, tls, tlsv1, tlsv11, tlsv12.
        # Default is tlsv12.
        tls_version = tlsv12

    # [[lwt]]
        # Turn lwt on and off.
        # Default is true.
        # enable = false

        # The topic that the will message should be published on.
        # Default is 'status'.
        # topic = 'status'

        # Default is 'online'.
        # online_payload ='online'

        # The message to send as a will.
        # Default is 'offline'.
        # offline_payload = offline

        # he quality of service level to use for the will.
        # Default is 0
        # qos = 0

        # If set to true, the will message will be set as the "last known good"/retained message for the topic.
        # The default is true.
        # retain = true

    # [[topics]]
        # [[[website/loop]]]
            # Controls if the topic is published.
            # Default is true.
            # publish = false

            # The format of the MQTT payload.
            # Currently support: individual, json, keyword
            # The default is 'json'
            # type = json

            # The binding, loop or archive.
            # Default is 'archive, loop'.
            # binding = loop

            # The QOS level to publish to.
            # Default is 0
            # qos = 1

            # The MQTT retain flag.
            # The default is False.
            # retain = true

            # The unit system for data published to this topic.
            # Options are US, METRIC or METRICWX
            # The default is US.
            # unit_system = US

            # True if all fields should not be published.
            # Useful if you only want select fields to be published
            # Valid values: True, False.
            # Default is  False
            # ignore = true

            # [[[[fields]]]]
                # [[[[[dateTime]]]]]
                    # Include the current dateTime value
                    # ignore = false

                # [[[[[outTemp]]]]]
                    # True if the field should not be published.
                    # Valid values: True, False.
                    # Default is  False
                    # ignore = true

                    # The WeeWX name of the data to be published.
                    # Default is the config section name.
                    # name = outTemp

                    # The WeeWX unit to convert the data being published to.
                    # Default is None.
                    # unit = degree_C

                    # Controls if data with a value of 'None' should be published.
                    # The default is false.
                    # publish_none_value = true

                    # Controls if the WeewX unit label should be append to the data being published.
                    # The default is true.
                    # append_unit_label = false

                    # The data type conversion to apply to the data being published.
                    # The default is not to convert.
                    # conversion_type = string

                    # The formatting to apply to the data being published.
                    # The default is '%s'.
                    # format_string = %s

        # [[[website/archive]]]
            # publish = false
            # type = json
            # binding = archive
            # qos = 1
            # retain = true
            # unit_system = METRIC
            # ignore = true

            # [[[[fields]]]]
                # [[[[[dateTime]]]]]
                    # ignore = false

                # [[[[[outTemp]]]]]
                    # ignore = false

        # [[[website/stats]]]
            # publish = false
            # type = json
            # binding = archive
            # qos = 1
            # retain = true
            # unit_system = METRICWX
            # ignore = true
            # minmax = both
            # day = true
            # yesterday = true
            # month = true
            # last_month = true
            # year = true
            # last_year = true
            # alltime = true

            # [[[[fields]]]]
                # [[[[[dateTime]]]]]
                    # ignore = false

                # [[[[[outTemp]]]]]
                    # ignore = false
"""

def loader():
    """ Load and return the extension installer. """
    return MQTTPublishInstaller()


class MQTTPublishInstaller(ExtensionInstaller):
    """ The extension installer. """
    def __init__(self):

        install_dict = {
            'version': VERSION,
            'name': 'MQTTPublishV2',
            # add a leading space, so that long versions do not run into the description
            'description': ' Publish WeeWX data to a MQTT broker.',
            'author': 'John Smith',
            'author_email': "deltafoxtrot256+MQTTPublishV2@gmail.com",
            'files': [('bin/user', ['bin/user/MQTTPublishV2.py'])],
            'config': configobj.ConfigObj(StringIO(CONFIG)),
            'restful_services': 'user.MQTTPublishV2.PublishWeeWX',
        }

        super().__init__(install_dict)
