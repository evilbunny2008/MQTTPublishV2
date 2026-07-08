<!-- markdownlint-disable first-line-heading  -->

## Description

A Weewx service publishes data to multiple MQTT topics.

Currently MQTT payloads of json, keyword (field1=value, field2=value..), and individual (each topic contains a single observation) are supported.

## Preqrequisites

|Prerequisite                                                   |Version                  |
|---------------------------------------------------------------|-------------------------|
|[WeeWX](https://www.weewx.com)                                 |5.0.0 or higher          |
|[Python](https://www.python.org)                               |3.9.13 or higher         |
|[Paho MQTT Python client](https://pypi.org/project/paho-mqtt/) |1.6.1 or higher          |
|[MQTT](https://mqtt.org)                                       |3.1, 3.1.1, 5 or higher. |

*Note:* Early versions of Python 3 may work, but have not been explicitly tested.

*Note:* Not all 'supported' versions of the Paho MQTT client have been tested.

*Note:* Not all 'supported' versions of MQTT have been tested.

## Installing

This extension is installed using the [weectl extension utility](https://www.weewx.com/docs/5.0/utilities/weectl-extension/).
The latest release can be installed with the invocation

```shell
weectl extension install https://github.com/evilbunny2008/MQTTPublishV2/archive/refs/tags/latest.zip
```

If a specific version is desired, the invocation would look like

```shell
weectl extension install https://github.com/evilbunny2008/MQTTPublishV2/archive/refs/tags/vX.Y.Z.zip
```

where X.Y.Z is the release.
The list of releases can be found at [https://github.com/evilbunny2008/MQTTPublishV2/releases](https://github.com/evilbunny2008/MQTTPublishV2/releases).

The version under development can be installed from the master branch using the following invocation

```shell
weectl extension install https://github.com/evilbunny2008/MQTTPublishV2/archive/master.zip
```

Where `master` is the branch name.

*Note:* WeeWX 'package' installs add the user that performed the install to the `weewx` group.
This means that this user should not need to use `sudo` to install the `weewx-mqtt/publish` extension.
**But** in order to for this update to the `weewx` group to take affect, the user has to have logged out/in at least once or use one of the other methods that can be found on the web

*Note:* WeeWX pip installs that install WeeWX into a `Python virtual environment`, must 'activate' the environment performing the install. A typical invocation would look like this.

```shell
source ~/weewx-venv/bin/activate
```

## Configuring

See the [weewx-sample.conf](https://github.com/evilbunny2008/MQTTPublishV2/blob/main/weewx-sample.conf) for an example stanze
