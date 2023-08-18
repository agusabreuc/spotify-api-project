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
from swagger_client.models.album_base import AlbumBase  # noqa: F401,E501

class SimplifiedAlbumObject(AlbumBase):
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
        'album_group': 'str',
        'artists': 'list[SimplifiedArtistObject]'
    }
    if hasattr(AlbumBase, "swagger_types"):
        swagger_types.update(AlbumBase.swagger_types)

    attribute_map = {
        'album_group': 'album_group',
        'artists': 'artists'
    }
    if hasattr(AlbumBase, "attribute_map"):
        attribute_map.update(AlbumBase.attribute_map)

    def __init__(self, album_group=None, artists=None, *args, **kwargs):  # noqa: E501
        """SimplifiedAlbumObject - a model defined in Swagger"""  # noqa: E501
        self._album_group = None
        self._artists = None
        self.discriminator = None
        if album_group is not None:
            self.album_group = album_group
        self.artists = artists
        AlbumBase.__init__(self, *args, **kwargs)

    @property
    def album_group(self):
        """Gets the album_group of this SimplifiedAlbumObject.  # noqa: E501

        The field is present when getting an artist's albums. Compare to album_type this field represents relationship between the artist and the album.   # noqa: E501

        :return: The album_group of this SimplifiedAlbumObject.  # noqa: E501
        :rtype: str
        """
        return self._album_group

    @album_group.setter
    def album_group(self, album_group):
        """Sets the album_group of this SimplifiedAlbumObject.

        The field is present when getting an artist's albums. Compare to album_type this field represents relationship between the artist and the album.   # noqa: E501

        :param album_group: The album_group of this SimplifiedAlbumObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["album", "single", "compilation", "appears_on"]  # noqa: E501
        if album_group not in allowed_values:
            raise ValueError(
                "Invalid value for `album_group` ({0}), must be one of {1}"  # noqa: E501
                .format(album_group, allowed_values)
            )

        self._album_group = album_group

    @property
    def artists(self):
        """Gets the artists of this SimplifiedAlbumObject.  # noqa: E501

        The artists of the album. Each artist object includes a link in `href` to more detailed information about the artist.   # noqa: E501

        :return: The artists of this SimplifiedAlbumObject.  # noqa: E501
        :rtype: list[SimplifiedArtistObject]
        """
        return self._artists

    @artists.setter
    def artists(self, artists):
        """Sets the artists of this SimplifiedAlbumObject.

        The artists of the album. Each artist object includes a link in `href` to more detailed information about the artist.   # noqa: E501

        :param artists: The artists of this SimplifiedAlbumObject.  # noqa: E501
        :type: list[SimplifiedArtistObject]
        """
        if artists is None:
            raise ValueError("Invalid value for `artists`, must not be `None`")  # noqa: E501

        self._artists = artists

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
        if issubclass(SimplifiedAlbumObject, dict):
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
        if not isinstance(other, SimplifiedAlbumObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
