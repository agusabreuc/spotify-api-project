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

class AudiobookBase(object):
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
        'authors': 'list[AuthorObject]',
        'available_markets': 'list[str]',
        'copyrights': 'list[CopyrightObject]',
        'description': 'str',
        'html_description': 'str',
        'edition': 'str',
        'explicit': 'bool',
        'external_urls': 'AllOfAudiobookBaseExternalUrls',
        'href': 'str',
        'id': 'str',
        'images': 'list[ImageObject]',
        'languages': 'list[str]',
        'media_type': 'str',
        'name': 'str',
        'narrators': 'list[NarratorObject]',
        'publisher': 'str',
        'type': 'str',
        'uri': 'str',
        'total_chapters': 'int'
    }

    attribute_map = {
        'authors': 'authors',
        'available_markets': 'available_markets',
        'copyrights': 'copyrights',
        'description': 'description',
        'html_description': 'html_description',
        'edition': 'edition',
        'explicit': 'explicit',
        'external_urls': 'external_urls',
        'href': 'href',
        'id': 'id',
        'images': 'images',
        'languages': 'languages',
        'media_type': 'media_type',
        'name': 'name',
        'narrators': 'narrators',
        'publisher': 'publisher',
        'type': 'type',
        'uri': 'uri',
        'total_chapters': 'total_chapters'
    }

    def __init__(self, authors=None, available_markets=None, copyrights=None, description=None, html_description=None, edition=None, explicit=None, external_urls=None, href=None, id=None, images=None, languages=None, media_type=None, name=None, narrators=None, publisher=None, type=None, uri=None, total_chapters=None):  # noqa: E501
        """AudiobookBase - a model defined in Swagger"""  # noqa: E501
        self._authors = None
        self._available_markets = None
        self._copyrights = None
        self._description = None
        self._html_description = None
        self._edition = None
        self._explicit = None
        self._external_urls = None
        self._href = None
        self._id = None
        self._images = None
        self._languages = None
        self._media_type = None
        self._name = None
        self._narrators = None
        self._publisher = None
        self._type = None
        self._uri = None
        self._total_chapters = None
        self.discriminator = None
        self.authors = authors
        self.available_markets = available_markets
        self.copyrights = copyrights
        self.description = description
        self.html_description = html_description
        if edition is not None:
            self.edition = edition
        self.explicit = explicit
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = images
        self.languages = languages
        self.media_type = media_type
        self.name = name
        self.narrators = narrators
        self.publisher = publisher
        self.type = type
        self.uri = uri
        self.total_chapters = total_chapters

    @property
    def authors(self):
        """Gets the authors of this AudiobookBase.  # noqa: E501

        The author(s) for the audiobook.   # noqa: E501

        :return: The authors of this AudiobookBase.  # noqa: E501
        :rtype: list[AuthorObject]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this AudiobookBase.

        The author(s) for the audiobook.   # noqa: E501

        :param authors: The authors of this AudiobookBase.  # noqa: E501
        :type: list[AuthorObject]
        """
        if authors is None:
            raise ValueError("Invalid value for `authors`, must not be `None`")  # noqa: E501

        self._authors = authors

    @property
    def available_markets(self):
        """Gets the available_markets of this AudiobookBase.  # noqa: E501

        A list of the countries in which the audiobook can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.   # noqa: E501

        :return: The available_markets of this AudiobookBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_markets

    @available_markets.setter
    def available_markets(self, available_markets):
        """Sets the available_markets of this AudiobookBase.

        A list of the countries in which the audiobook can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.   # noqa: E501

        :param available_markets: The available_markets of this AudiobookBase.  # noqa: E501
        :type: list[str]
        """
        if available_markets is None:
            raise ValueError("Invalid value for `available_markets`, must not be `None`")  # noqa: E501

        self._available_markets = available_markets

    @property
    def copyrights(self):
        """Gets the copyrights of this AudiobookBase.  # noqa: E501

        The copyright statements of the audiobook.   # noqa: E501

        :return: The copyrights of this AudiobookBase.  # noqa: E501
        :rtype: list[CopyrightObject]
        """
        return self._copyrights

    @copyrights.setter
    def copyrights(self, copyrights):
        """Sets the copyrights of this AudiobookBase.

        The copyright statements of the audiobook.   # noqa: E501

        :param copyrights: The copyrights of this AudiobookBase.  # noqa: E501
        :type: list[CopyrightObject]
        """
        if copyrights is None:
            raise ValueError("Invalid value for `copyrights`, must not be `None`")  # noqa: E501

        self._copyrights = copyrights

    @property
    def description(self):
        """Gets the description of this AudiobookBase.  # noqa: E501

        A description of the audiobook. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed.   # noqa: E501

        :return: The description of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AudiobookBase.

        A description of the audiobook. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed.   # noqa: E501

        :param description: The description of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def html_description(self):
        """Gets the html_description of this AudiobookBase.  # noqa: E501

        A description of the audiobook. This field may contain HTML tags.   # noqa: E501

        :return: The html_description of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._html_description

    @html_description.setter
    def html_description(self, html_description):
        """Sets the html_description of this AudiobookBase.

        A description of the audiobook. This field may contain HTML tags.   # noqa: E501

        :param html_description: The html_description of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if html_description is None:
            raise ValueError("Invalid value for `html_description`, must not be `None`")  # noqa: E501

        self._html_description = html_description

    @property
    def edition(self):
        """Gets the edition of this AudiobookBase.  # noqa: E501

        The edition of the audiobook.   # noqa: E501

        :return: The edition of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this AudiobookBase.

        The edition of the audiobook.   # noqa: E501

        :param edition: The edition of this AudiobookBase.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def explicit(self):
        """Gets the explicit of this AudiobookBase.  # noqa: E501

        Whether or not the audiobook has explicit content (true = yes it does; false = no it does not OR unknown).   # noqa: E501

        :return: The explicit of this AudiobookBase.  # noqa: E501
        :rtype: bool
        """
        return self._explicit

    @explicit.setter
    def explicit(self, explicit):
        """Sets the explicit of this AudiobookBase.

        Whether or not the audiobook has explicit content (true = yes it does; false = no it does not OR unknown).   # noqa: E501

        :param explicit: The explicit of this AudiobookBase.  # noqa: E501
        :type: bool
        """
        if explicit is None:
            raise ValueError("Invalid value for `explicit`, must not be `None`")  # noqa: E501

        self._explicit = explicit

    @property
    def external_urls(self):
        """Gets the external_urls of this AudiobookBase.  # noqa: E501

        External URLs for this audiobook.   # noqa: E501

        :return: The external_urls of this AudiobookBase.  # noqa: E501
        :rtype: AllOfAudiobookBaseExternalUrls
        """
        return self._external_urls

    @external_urls.setter
    def external_urls(self, external_urls):
        """Sets the external_urls of this AudiobookBase.

        External URLs for this audiobook.   # noqa: E501

        :param external_urls: The external_urls of this AudiobookBase.  # noqa: E501
        :type: AllOfAudiobookBaseExternalUrls
        """
        if external_urls is None:
            raise ValueError("Invalid value for `external_urls`, must not be `None`")  # noqa: E501

        self._external_urls = external_urls

    @property
    def href(self):
        """Gets the href of this AudiobookBase.  # noqa: E501

        A link to the Web API endpoint providing full details of the audiobook.   # noqa: E501

        :return: The href of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AudiobookBase.

        A link to the Web API endpoint providing full details of the audiobook.   # noqa: E501

        :param href: The href of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def id(self):
        """Gets the id of this AudiobookBase.  # noqa: E501

        The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook.   # noqa: E501

        :return: The id of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AudiobookBase.

        The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook.   # noqa: E501

        :param id: The id of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def images(self):
        """Gets the images of this AudiobookBase.  # noqa: E501

        The cover art for the audiobook in various sizes, widest first.   # noqa: E501

        :return: The images of this AudiobookBase.  # noqa: E501
        :rtype: list[ImageObject]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this AudiobookBase.

        The cover art for the audiobook in various sizes, widest first.   # noqa: E501

        :param images: The images of this AudiobookBase.  # noqa: E501
        :type: list[ImageObject]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def languages(self):
        """Gets the languages of this AudiobookBase.  # noqa: E501

        A list of the languages used in the audiobook, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.   # noqa: E501

        :return: The languages of this AudiobookBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this AudiobookBase.

        A list of the languages used in the audiobook, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.   # noqa: E501

        :param languages: The languages of this AudiobookBase.  # noqa: E501
        :type: list[str]
        """
        if languages is None:
            raise ValueError("Invalid value for `languages`, must not be `None`")  # noqa: E501

        self._languages = languages

    @property
    def media_type(self):
        """Gets the media_type of this AudiobookBase.  # noqa: E501

        The media type of the audiobook.   # noqa: E501

        :return: The media_type of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this AudiobookBase.

        The media type of the audiobook.   # noqa: E501

        :param media_type: The media_type of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")  # noqa: E501

        self._media_type = media_type

    @property
    def name(self):
        """Gets the name of this AudiobookBase.  # noqa: E501

        The name of the audiobook.   # noqa: E501

        :return: The name of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AudiobookBase.

        The name of the audiobook.   # noqa: E501

        :param name: The name of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def narrators(self):
        """Gets the narrators of this AudiobookBase.  # noqa: E501

        The narrator(s) for the audiobook.   # noqa: E501

        :return: The narrators of this AudiobookBase.  # noqa: E501
        :rtype: list[NarratorObject]
        """
        return self._narrators

    @narrators.setter
    def narrators(self, narrators):
        """Sets the narrators of this AudiobookBase.

        The narrator(s) for the audiobook.   # noqa: E501

        :param narrators: The narrators of this AudiobookBase.  # noqa: E501
        :type: list[NarratorObject]
        """
        if narrators is None:
            raise ValueError("Invalid value for `narrators`, must not be `None`")  # noqa: E501

        self._narrators = narrators

    @property
    def publisher(self):
        """Gets the publisher of this AudiobookBase.  # noqa: E501

        The publisher of the audiobook.   # noqa: E501

        :return: The publisher of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this AudiobookBase.

        The publisher of the audiobook.   # noqa: E501

        :param publisher: The publisher of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if publisher is None:
            raise ValueError("Invalid value for `publisher`, must not be `None`")  # noqa: E501

        self._publisher = publisher

    @property
    def type(self):
        """Gets the type of this AudiobookBase.  # noqa: E501

        The object type.   # noqa: E501

        :return: The type of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AudiobookBase.

        The object type.   # noqa: E501

        :param type: The type of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["audiobook"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this AudiobookBase.  # noqa: E501

        The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook.   # noqa: E501

        :return: The uri of this AudiobookBase.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this AudiobookBase.

        The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook.   # noqa: E501

        :param uri: The uri of this AudiobookBase.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def total_chapters(self):
        """Gets the total_chapters of this AudiobookBase.  # noqa: E501

        The number of chapters in this audiobook.   # noqa: E501

        :return: The total_chapters of this AudiobookBase.  # noqa: E501
        :rtype: int
        """
        return self._total_chapters

    @total_chapters.setter
    def total_chapters(self, total_chapters):
        """Sets the total_chapters of this AudiobookBase.

        The number of chapters in this audiobook.   # noqa: E501

        :param total_chapters: The total_chapters of this AudiobookBase.  # noqa: E501
        :type: int
        """
        if total_chapters is None:
            raise ValueError("Invalid value for `total_chapters`, must not be `None`")  # noqa: E501

        self._total_chapters = total_chapters

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
        if issubclass(AudiobookBase, dict):
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
        if not isinstance(other, AudiobookBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
