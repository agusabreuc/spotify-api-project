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

class DisallowsObject(object):
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
        'interrupting_playback': 'bool',
        'pausing': 'bool',
        'resuming': 'bool',
        'seeking': 'bool',
        'skipping_next': 'bool',
        'skipping_prev': 'bool',
        'toggling_repeat_context': 'bool',
        'toggling_shuffle': 'bool',
        'toggling_repeat_track': 'bool',
        'transferring_playback': 'bool'
    }

    attribute_map = {
        'interrupting_playback': 'interrupting_playback',
        'pausing': 'pausing',
        'resuming': 'resuming',
        'seeking': 'seeking',
        'skipping_next': 'skipping_next',
        'skipping_prev': 'skipping_prev',
        'toggling_repeat_context': 'toggling_repeat_context',
        'toggling_shuffle': 'toggling_shuffle',
        'toggling_repeat_track': 'toggling_repeat_track',
        'transferring_playback': 'transferring_playback'
    }

    def __init__(self, interrupting_playback=None, pausing=None, resuming=None, seeking=None, skipping_next=None, skipping_prev=None, toggling_repeat_context=None, toggling_shuffle=None, toggling_repeat_track=None, transferring_playback=None):  # noqa: E501
        """DisallowsObject - a model defined in Swagger"""  # noqa: E501
        self._interrupting_playback = None
        self._pausing = None
        self._resuming = None
        self._seeking = None
        self._skipping_next = None
        self._skipping_prev = None
        self._toggling_repeat_context = None
        self._toggling_shuffle = None
        self._toggling_repeat_track = None
        self._transferring_playback = None
        self.discriminator = None
        if interrupting_playback is not None:
            self.interrupting_playback = interrupting_playback
        if pausing is not None:
            self.pausing = pausing
        if resuming is not None:
            self.resuming = resuming
        if seeking is not None:
            self.seeking = seeking
        if skipping_next is not None:
            self.skipping_next = skipping_next
        if skipping_prev is not None:
            self.skipping_prev = skipping_prev
        if toggling_repeat_context is not None:
            self.toggling_repeat_context = toggling_repeat_context
        if toggling_shuffle is not None:
            self.toggling_shuffle = toggling_shuffle
        if toggling_repeat_track is not None:
            self.toggling_repeat_track = toggling_repeat_track
        if transferring_playback is not None:
            self.transferring_playback = transferring_playback

    @property
    def interrupting_playback(self):
        """Gets the interrupting_playback of this DisallowsObject.  # noqa: E501

        Interrupting playback. Optional field.  # noqa: E501

        :return: The interrupting_playback of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._interrupting_playback

    @interrupting_playback.setter
    def interrupting_playback(self, interrupting_playback):
        """Sets the interrupting_playback of this DisallowsObject.

        Interrupting playback. Optional field.  # noqa: E501

        :param interrupting_playback: The interrupting_playback of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._interrupting_playback = interrupting_playback

    @property
    def pausing(self):
        """Gets the pausing of this DisallowsObject.  # noqa: E501

        Pausing. Optional field.  # noqa: E501

        :return: The pausing of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._pausing

    @pausing.setter
    def pausing(self, pausing):
        """Sets the pausing of this DisallowsObject.

        Pausing. Optional field.  # noqa: E501

        :param pausing: The pausing of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._pausing = pausing

    @property
    def resuming(self):
        """Gets the resuming of this DisallowsObject.  # noqa: E501

        Resuming. Optional field.  # noqa: E501

        :return: The resuming of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._resuming

    @resuming.setter
    def resuming(self, resuming):
        """Sets the resuming of this DisallowsObject.

        Resuming. Optional field.  # noqa: E501

        :param resuming: The resuming of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._resuming = resuming

    @property
    def seeking(self):
        """Gets the seeking of this DisallowsObject.  # noqa: E501

        Seeking playback location. Optional field.  # noqa: E501

        :return: The seeking of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._seeking

    @seeking.setter
    def seeking(self, seeking):
        """Sets the seeking of this DisallowsObject.

        Seeking playback location. Optional field.  # noqa: E501

        :param seeking: The seeking of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._seeking = seeking

    @property
    def skipping_next(self):
        """Gets the skipping_next of this DisallowsObject.  # noqa: E501

        Skipping to the next context. Optional field.  # noqa: E501

        :return: The skipping_next of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._skipping_next

    @skipping_next.setter
    def skipping_next(self, skipping_next):
        """Sets the skipping_next of this DisallowsObject.

        Skipping to the next context. Optional field.  # noqa: E501

        :param skipping_next: The skipping_next of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._skipping_next = skipping_next

    @property
    def skipping_prev(self):
        """Gets the skipping_prev of this DisallowsObject.  # noqa: E501

        Skipping to the previous context. Optional field.  # noqa: E501

        :return: The skipping_prev of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._skipping_prev

    @skipping_prev.setter
    def skipping_prev(self, skipping_prev):
        """Sets the skipping_prev of this DisallowsObject.

        Skipping to the previous context. Optional field.  # noqa: E501

        :param skipping_prev: The skipping_prev of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._skipping_prev = skipping_prev

    @property
    def toggling_repeat_context(self):
        """Gets the toggling_repeat_context of this DisallowsObject.  # noqa: E501

        Toggling repeat context flag. Optional field.  # noqa: E501

        :return: The toggling_repeat_context of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._toggling_repeat_context

    @toggling_repeat_context.setter
    def toggling_repeat_context(self, toggling_repeat_context):
        """Sets the toggling_repeat_context of this DisallowsObject.

        Toggling repeat context flag. Optional field.  # noqa: E501

        :param toggling_repeat_context: The toggling_repeat_context of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._toggling_repeat_context = toggling_repeat_context

    @property
    def toggling_shuffle(self):
        """Gets the toggling_shuffle of this DisallowsObject.  # noqa: E501

        Toggling shuffle flag. Optional field.  # noqa: E501

        :return: The toggling_shuffle of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._toggling_shuffle

    @toggling_shuffle.setter
    def toggling_shuffle(self, toggling_shuffle):
        """Sets the toggling_shuffle of this DisallowsObject.

        Toggling shuffle flag. Optional field.  # noqa: E501

        :param toggling_shuffle: The toggling_shuffle of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._toggling_shuffle = toggling_shuffle

    @property
    def toggling_repeat_track(self):
        """Gets the toggling_repeat_track of this DisallowsObject.  # noqa: E501

        Toggling repeat track flag. Optional field.  # noqa: E501

        :return: The toggling_repeat_track of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._toggling_repeat_track

    @toggling_repeat_track.setter
    def toggling_repeat_track(self, toggling_repeat_track):
        """Sets the toggling_repeat_track of this DisallowsObject.

        Toggling repeat track flag. Optional field.  # noqa: E501

        :param toggling_repeat_track: The toggling_repeat_track of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._toggling_repeat_track = toggling_repeat_track

    @property
    def transferring_playback(self):
        """Gets the transferring_playback of this DisallowsObject.  # noqa: E501

        Transfering playback between devices. Optional field.  # noqa: E501

        :return: The transferring_playback of this DisallowsObject.  # noqa: E501
        :rtype: bool
        """
        return self._transferring_playback

    @transferring_playback.setter
    def transferring_playback(self, transferring_playback):
        """Sets the transferring_playback of this DisallowsObject.

        Transfering playback between devices. Optional field.  # noqa: E501

        :param transferring_playback: The transferring_playback of this DisallowsObject.  # noqa: E501
        :type: bool
        """

        self._transferring_playback = transferring_playback

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
        if issubclass(DisallowsObject, dict):
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
        if not isinstance(other, DisallowsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other