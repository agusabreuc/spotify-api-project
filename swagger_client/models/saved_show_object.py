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

class SavedShowObject(object):
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
        'added_at': 'datetime',
        'show': 'AllOfSavedShowObjectShow'
    }

    attribute_map = {
        'added_at': 'added_at',
        'show': 'show'
    }

    def __init__(self, added_at=None, show=None):  # noqa: E501
        """SavedShowObject - a model defined in Swagger"""  # noqa: E501
        self._added_at = None
        self._show = None
        self.discriminator = None
        if added_at is not None:
            self.added_at = added_at
        if show is not None:
            self.show = show

    @property
    def added_at(self):
        """Gets the added_at of this SavedShowObject.  # noqa: E501

        The date and time the show was saved. Timestamps are returned in ISO 8601 format as Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is imprecise (for example, the date/time of an album release), an additional field indicates the precision; see for example, release_date in an album object.   # noqa: E501

        :return: The added_at of this SavedShowObject.  # noqa: E501
        :rtype: datetime
        """
        return self._added_at

    @added_at.setter
    def added_at(self, added_at):
        """Sets the added_at of this SavedShowObject.

        The date and time the show was saved. Timestamps are returned in ISO 8601 format as Coordinated Universal Time (UTC) with a zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is imprecise (for example, the date/time of an album release), an additional field indicates the precision; see for example, release_date in an album object.   # noqa: E501

        :param added_at: The added_at of this SavedShowObject.  # noqa: E501
        :type: datetime
        """

        self._added_at = added_at

    @property
    def show(self):
        """Gets the show of this SavedShowObject.  # noqa: E501

        Information about the show.  # noqa: E501

        :return: The show of this SavedShowObject.  # noqa: E501
        :rtype: AllOfSavedShowObjectShow
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this SavedShowObject.

        Information about the show.  # noqa: E501

        :param show: The show of this SavedShowObject.  # noqa: E501
        :type: AllOfSavedShowObjectShow
        """

        self._show = show

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
        if issubclass(SavedShowObject, dict):
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
        if not isinstance(other, SavedShowObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
