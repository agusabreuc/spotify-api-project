# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CurrentlyPlayingContextObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device': 'AllOfCurrentlyPlayingContextObjectDevice',
        'repeat_state': 'str',
        'shuffle_state': 'bool',
        'context': 'AllOfCurrentlyPlayingContextObjectContext',
        'timestamp': 'int',
        'progress_ms': 'int',
        'is_playing': 'bool',
        'item': 'OneOfCurrentlyPlayingContextObjectItem',
        'currently_playing_type': 'str',
        'actions': 'AllOfCurrentlyPlayingContextObjectActions'
    }

    attribute_map = {
        'device': 'device',
        'repeat_state': 'repeat_state',
        'shuffle_state': 'shuffle_state',
        'context': 'context',
        'timestamp': 'timestamp',
        'progress_ms': 'progress_ms',
        'is_playing': 'is_playing',
        'item': 'item',
        'currently_playing_type': 'currently_playing_type',
        'actions': 'actions'
    }

    def __init__(self, device=None, repeat_state=None, shuffle_state=None, context=None, timestamp=None, progress_ms=None, is_playing=None, item=None, currently_playing_type=None, actions=None):  # noqa: E501
        """CurrentlyPlayingContextObject - a model defined in Swagger"""  # noqa: E501
        self._device = None
        self._repeat_state = None
        self._shuffle_state = None
        self._context = None
        self._timestamp = None
        self._progress_ms = None
        self._is_playing = None
        self._item = None
        self._currently_playing_type = None
        self._actions = None
        self.discriminator = None
        if device is not None:
            self.device = device
        if repeat_state is not None:
            self.repeat_state = repeat_state
        if shuffle_state is not None:
            self.shuffle_state = shuffle_state
        if context is not None:
            self.context = context
        if timestamp is not None:
            self.timestamp = timestamp
        if progress_ms is not None:
            self.progress_ms = progress_ms
        if is_playing is not None:
            self.is_playing = is_playing
        if item is not None:
            self.item = item
        if currently_playing_type is not None:
            self.currently_playing_type = currently_playing_type
        if actions is not None:
            self.actions = actions

    @property
    def device(self):
        """Gets the device of this CurrentlyPlayingContextObject.  # noqa: E501

        The device that is currently active.   # noqa: E501

        :return: The device of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: AllOfCurrentlyPlayingContextObjectDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this CurrentlyPlayingContextObject.

        The device that is currently active.   # noqa: E501

        :param device: The device of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: AllOfCurrentlyPlayingContextObjectDevice
        """

        self._device = device

    @property
    def repeat_state(self):
        """Gets the repeat_state of this CurrentlyPlayingContextObject.  # noqa: E501

        off, track, context  # noqa: E501

        :return: The repeat_state of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: str
        """
        return self._repeat_state

    @repeat_state.setter
    def repeat_state(self, repeat_state):
        """Sets the repeat_state of this CurrentlyPlayingContextObject.

        off, track, context  # noqa: E501

        :param repeat_state: The repeat_state of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: str
        """

        self._repeat_state = repeat_state

    @property
    def shuffle_state(self):
        """Gets the shuffle_state of this CurrentlyPlayingContextObject.  # noqa: E501

        If shuffle is on or off.  # noqa: E501

        :return: The shuffle_state of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: bool
        """
        return self._shuffle_state

    @shuffle_state.setter
    def shuffle_state(self, shuffle_state):
        """Sets the shuffle_state of this CurrentlyPlayingContextObject.

        If shuffle is on or off.  # noqa: E501

        :param shuffle_state: The shuffle_state of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: bool
        """

        self._shuffle_state = shuffle_state

    @property
    def context(self):
        """Gets the context of this CurrentlyPlayingContextObject.  # noqa: E501

        A Context Object. Can be `null`.  # noqa: E501

        :return: The context of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: AllOfCurrentlyPlayingContextObjectContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this CurrentlyPlayingContextObject.

        A Context Object. Can be `null`.  # noqa: E501

        :param context: The context of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: AllOfCurrentlyPlayingContextObjectContext
        """

        self._context = context

    @property
    def timestamp(self):
        """Gets the timestamp of this CurrentlyPlayingContextObject.  # noqa: E501

        Unix Millisecond Timestamp when data was fetched.  # noqa: E501

        :return: The timestamp of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CurrentlyPlayingContextObject.

        Unix Millisecond Timestamp when data was fetched.  # noqa: E501

        :param timestamp: The timestamp of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def progress_ms(self):
        """Gets the progress_ms of this CurrentlyPlayingContextObject.  # noqa: E501

        Progress into the currently playing track or episode. Can be `null`.  # noqa: E501

        :return: The progress_ms of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: int
        """
        return self._progress_ms

    @progress_ms.setter
    def progress_ms(self, progress_ms):
        """Sets the progress_ms of this CurrentlyPlayingContextObject.

        Progress into the currently playing track or episode. Can be `null`.  # noqa: E501

        :param progress_ms: The progress_ms of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: int
        """

        self._progress_ms = progress_ms

    @property
    def is_playing(self):
        """Gets the is_playing of this CurrentlyPlayingContextObject.  # noqa: E501

        If something is currently playing, return `true`.  # noqa: E501

        :return: The is_playing of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_playing

    @is_playing.setter
    def is_playing(self, is_playing):
        """Sets the is_playing of this CurrentlyPlayingContextObject.

        If something is currently playing, return `true`.  # noqa: E501

        :param is_playing: The is_playing of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: bool
        """

        self._is_playing = is_playing

    @property
    def item(self):
        """Gets the item of this CurrentlyPlayingContextObject.  # noqa: E501

        The currently playing track or episode. Can be `null`.  # noqa: E501

        :return: The item of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: OneOfCurrentlyPlayingContextObjectItem
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this CurrentlyPlayingContextObject.

        The currently playing track or episode. Can be `null`.  # noqa: E501

        :param item: The item of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: OneOfCurrentlyPlayingContextObjectItem
        """

        self._item = item

    @property
    def currently_playing_type(self):
        """Gets the currently_playing_type of this CurrentlyPlayingContextObject.  # noqa: E501

        The object type of the currently playing item. Can be one of `track`, `episode`, `ad` or `unknown`.   # noqa: E501

        :return: The currently_playing_type of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: str
        """
        return self._currently_playing_type

    @currently_playing_type.setter
    def currently_playing_type(self, currently_playing_type):
        """Sets the currently_playing_type of this CurrentlyPlayingContextObject.

        The object type of the currently playing item. Can be one of `track`, `episode`, `ad` or `unknown`.   # noqa: E501

        :param currently_playing_type: The currently_playing_type of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: str
        """

        self._currently_playing_type = currently_playing_type

    @property
    def actions(self):
        """Gets the actions of this CurrentlyPlayingContextObject.  # noqa: E501

        Allows to update the user interface based on which playback actions are available within the current context.   # noqa: E501

        :return: The actions of this CurrentlyPlayingContextObject.  # noqa: E501
        :rtype: AllOfCurrentlyPlayingContextObjectActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CurrentlyPlayingContextObject.

        Allows to update the user interface based on which playback actions are available within the current context.   # noqa: E501

        :param actions: The actions of this CurrentlyPlayingContextObject.  # noqa: E501
        :type: AllOfCurrentlyPlayingContextObjectActions
        """

        self._actions = actions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CurrentlyPlayingContextObject, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CurrentlyPlayingContextObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other