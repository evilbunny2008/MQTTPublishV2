#    Copyright (c) 2025 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

""" Installer for MQTTPublishV2 service.

To uninstall run
weectl extension uninstall MQTTPublishV2
"""

from io import StringIO

from weecfg.extension import ExtensionInstaller

VERSION = "2.1.3"

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
            'restful_services': 'user.MQTTPublishV2.PublishWeeWX',
        }

        super().__init__(install_dict)
