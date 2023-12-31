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

class LinkedTrackObject(object):
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
        'external_urls': 'AllOfLinkedTrackObjectExternalUrls',
        'href': 'str',
        'id': 'str',
        'type': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'external_urls': 'external_urls',
        'href': 'href',
        'id': 'id',
        'type': 'type',
        'uri': 'uri'
    }

    def __init__(self, external_urls=None, href=None, id=None, type=None, uri=None):  # noqa: E501
        """LinkedTrackObject - a model defined in Swagger"""  # noqa: E501
        self._external_urls = None
        self._href = None
        self._id = None
        self._type = None
        self._uri = None
        self.discriminator = None
        if external_urls is not None:
            self.external_urls = external_urls
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if uri is not None:
            self.uri = uri

    @property
    def external_urls(self):
        """Gets the external_urls of this LinkedTrackObject.  # noqa: E501

        Known external URLs for this track.   # noqa: E501

        :return: The external_urls of this LinkedTrackObject.  # noqa: E501
        :rtype: AllOfLinkedTrackObjectExternalUrls
        """
        return self._external_urls

    @external_urls.setter
    def external_urls(self, external_urls):
        """Sets the external_urls of this LinkedTrackObject.

        Known external URLs for this track.   # noqa: E501

        :param external_urls: The external_urls of this LinkedTrackObject.  # noqa: E501
        :type: AllOfLinkedTrackObjectExternalUrls
        """

        self._external_urls = external_urls

    @property
    def href(self):
        """Gets the href of this LinkedTrackObject.  # noqa: E501

        A link to the Web API endpoint providing full details of the track.   # noqa: E501

        :return: The href of this LinkedTrackObject.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LinkedTrackObject.

        A link to the Web API endpoint providing full details of the track.   # noqa: E501

        :param href: The href of this LinkedTrackObject.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this LinkedTrackObject.  # noqa: E501

        The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track.   # noqa: E501

        :return: The id of this LinkedTrackObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LinkedTrackObject.

        The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the track.   # noqa: E501

        :param id: The id of this LinkedTrackObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LinkedTrackObject.  # noqa: E501

        The object type: \"track\".   # noqa: E501

        :return: The type of this LinkedTrackObject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LinkedTrackObject.

        The object type: \"track\".   # noqa: E501

        :param type: The type of this LinkedTrackObject.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this LinkedTrackObject.  # noqa: E501

        The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track.   # noqa: E501

        :return: The uri of this LinkedTrackObject.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this LinkedTrackObject.

        The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the track.   # noqa: E501

        :param uri: The uri of this LinkedTrackObject.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(LinkedTrackObject, dict):
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
        if not isinstance(other, LinkedTrackObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
