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

class ChapterBase(object):
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
        'audio_preview_url': 'str',
        'available_markets': 'list[str]',
        'chapter_number': 'int',
        'description': 'str',
        'html_description': 'str',
        'duration_ms': 'int',
        'explicit': 'bool',
        'external_urls': 'AllOfChapterBaseExternalUrls',
        'href': 'str',
        'id': 'str',
        'images': 'list[ImageObject]',
        'is_playable': 'bool',
        'languages': 'list[str]',
        'name': 'str',
        'release_date': 'str',
        'release_date_precision': 'str',
        'resume_point': 'AllOfChapterBaseResumePoint',
        'type': 'str',
        'uri': 'str',
        'restrictions': 'AllOfChapterBaseRestrictions'
    }

    attribute_map = {
        'audio_preview_url': 'audio_preview_url',
        'available_markets': 'available_markets',
        'chapter_number': 'chapter_number',
        'description': 'description',
        'html_description': 'html_description',
        'duration_ms': 'duration_ms',
        'explicit': 'explicit',
        'external_urls': 'external_urls',
        'href': 'href',
        'id': 'id',
        'images': 'images',
        'is_playable': 'is_playable',
        'languages': 'languages',
        'name': 'name',
        'release_date': 'release_date',
        'release_date_precision': 'release_date_precision',
        'resume_point': 'resume_point',
        'type': 'type',
        'uri': 'uri',
        'restrictions': 'restrictions'
    }

    def __init__(self, audio_preview_url=None, available_markets=None, chapter_number=None, description=None, html_description=None, duration_ms=None, explicit=None, external_urls=None, href=None, id=None, images=None, is_playable=None, languages=None, name=None, release_date=None, release_date_precision=None, resume_point=None, type=None, uri=None, restrictions=None):  # noqa: E501
        """ChapterBase - a model defined in Swagger"""  # noqa: E501
        self._audio_preview_url = None
        self._available_markets = None
        self._chapter_number = None
        self._description = None
        self._html_description = None
        self._duration_ms = None
        self._explicit = None
        self._external_urls = None
        self._href = None
        self._id = None
        self._images = None
        self._is_playable = None
        self._languages = None
        self._name = None
        self._release_date = None
        self._release_date_precision = None
        self._resume_point = None
        self._type = None
        self._uri = None
        self._restrictions = None
        self.discriminator = None
        self.audio_preview_url = audio_preview_url
        if available_markets is not None:
            self.available_markets = available_markets
        self.chapter_number = chapter_number
        self.description = description
        self.html_description = html_description
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.images = images
        self.is_playable = is_playable
        self.languages = languages
        self.name = name
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.resume_point = resume_point
        self.type = type
        self.uri = uri
        if restrictions is not None:
            self.restrictions = restrictions

    @property
    def audio_preview_url(self):
        """Gets the audio_preview_url of this ChapterBase.  # noqa: E501

        A URL to a 30 second preview (MP3 format) of the episode. `null` if not available.   # noqa: E501

        :return: The audio_preview_url of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._audio_preview_url

    @audio_preview_url.setter
    def audio_preview_url(self, audio_preview_url):
        """Sets the audio_preview_url of this ChapterBase.

        A URL to a 30 second preview (MP3 format) of the episode. `null` if not available.   # noqa: E501

        :param audio_preview_url: The audio_preview_url of this ChapterBase.  # noqa: E501
        :type: str
        """
        if audio_preview_url is None:
            raise ValueError("Invalid value for `audio_preview_url`, must not be `None`")  # noqa: E501

        self._audio_preview_url = audio_preview_url

    @property
    def available_markets(self):
        """Gets the available_markets of this ChapterBase.  # noqa: E501

        A list of the countries in which the chapter can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.   # noqa: E501

        :return: The available_markets of this ChapterBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_markets

    @available_markets.setter
    def available_markets(self, available_markets):
        """Sets the available_markets of this ChapterBase.

        A list of the countries in which the chapter can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.   # noqa: E501

        :param available_markets: The available_markets of this ChapterBase.  # noqa: E501
        :type: list[str]
        """

        self._available_markets = available_markets

    @property
    def chapter_number(self):
        """Gets the chapter_number of this ChapterBase.  # noqa: E501

        The number of the chapter   # noqa: E501

        :return: The chapter_number of this ChapterBase.  # noqa: E501
        :rtype: int
        """
        return self._chapter_number

    @chapter_number.setter
    def chapter_number(self, chapter_number):
        """Sets the chapter_number of this ChapterBase.

        The number of the chapter   # noqa: E501

        :param chapter_number: The chapter_number of this ChapterBase.  # noqa: E501
        :type: int
        """
        if chapter_number is None:
            raise ValueError("Invalid value for `chapter_number`, must not be `None`")  # noqa: E501

        self._chapter_number = chapter_number

    @property
    def description(self):
        """Gets the description of this ChapterBase.  # noqa: E501

        A description of the episode. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed.   # noqa: E501

        :return: The description of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChapterBase.

        A description of the episode. HTML tags are stripped away from this field, use `html_description` field in case HTML tags are needed.   # noqa: E501

        :param description: The description of this ChapterBase.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def html_description(self):
        """Gets the html_description of this ChapterBase.  # noqa: E501

        A description of the episode. This field may contain HTML tags.   # noqa: E501

        :return: The html_description of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._html_description

    @html_description.setter
    def html_description(self, html_description):
        """Sets the html_description of this ChapterBase.

        A description of the episode. This field may contain HTML tags.   # noqa: E501

        :param html_description: The html_description of this ChapterBase.  # noqa: E501
        :type: str
        """
        if html_description is None:
            raise ValueError("Invalid value for `html_description`, must not be `None`")  # noqa: E501

        self._html_description = html_description

    @property
    def duration_ms(self):
        """Gets the duration_ms of this ChapterBase.  # noqa: E501

        The episode length in milliseconds.   # noqa: E501

        :return: The duration_ms of this ChapterBase.  # noqa: E501
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        """Sets the duration_ms of this ChapterBase.

        The episode length in milliseconds.   # noqa: E501

        :param duration_ms: The duration_ms of this ChapterBase.  # noqa: E501
        :type: int
        """
        if duration_ms is None:
            raise ValueError("Invalid value for `duration_ms`, must not be `None`")  # noqa: E501

        self._duration_ms = duration_ms

    @property
    def explicit(self):
        """Gets the explicit of this ChapterBase.  # noqa: E501

        Whether or not the episode has explicit content (true = yes it does; false = no it does not OR unknown).   # noqa: E501

        :return: The explicit of this ChapterBase.  # noqa: E501
        :rtype: bool
        """
        return self._explicit

    @explicit.setter
    def explicit(self, explicit):
        """Sets the explicit of this ChapterBase.

        Whether or not the episode has explicit content (true = yes it does; false = no it does not OR unknown).   # noqa: E501

        :param explicit: The explicit of this ChapterBase.  # noqa: E501
        :type: bool
        """
        if explicit is None:
            raise ValueError("Invalid value for `explicit`, must not be `None`")  # noqa: E501

        self._explicit = explicit

    @property
    def external_urls(self):
        """Gets the external_urls of this ChapterBase.  # noqa: E501

        External URLs for this episode.   # noqa: E501

        :return: The external_urls of this ChapterBase.  # noqa: E501
        :rtype: AllOfChapterBaseExternalUrls
        """
        return self._external_urls

    @external_urls.setter
    def external_urls(self, external_urls):
        """Sets the external_urls of this ChapterBase.

        External URLs for this episode.   # noqa: E501

        :param external_urls: The external_urls of this ChapterBase.  # noqa: E501
        :type: AllOfChapterBaseExternalUrls
        """
        if external_urls is None:
            raise ValueError("Invalid value for `external_urls`, must not be `None`")  # noqa: E501

        self._external_urls = external_urls

    @property
    def href(self):
        """Gets the href of this ChapterBase.  # noqa: E501

        A link to the Web API endpoint providing full details of the episode.   # noqa: E501

        :return: The href of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ChapterBase.

        A link to the Web API endpoint providing full details of the episode.   # noqa: E501

        :param href: The href of this ChapterBase.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def id(self):
        """Gets the id of this ChapterBase.  # noqa: E501

        The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the episode.   # noqa: E501

        :return: The id of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChapterBase.

        The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the episode.   # noqa: E501

        :param id: The id of this ChapterBase.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def images(self):
        """Gets the images of this ChapterBase.  # noqa: E501

        The cover art for the episode in various sizes, widest first.   # noqa: E501

        :return: The images of this ChapterBase.  # noqa: E501
        :rtype: list[ImageObject]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this ChapterBase.

        The cover art for the episode in various sizes, widest first.   # noqa: E501

        :param images: The images of this ChapterBase.  # noqa: E501
        :type: list[ImageObject]
        """
        if images is None:
            raise ValueError("Invalid value for `images`, must not be `None`")  # noqa: E501

        self._images = images

    @property
    def is_playable(self):
        """Gets the is_playable of this ChapterBase.  # noqa: E501

        True if the episode is playable in the given market. Otherwise false.   # noqa: E501

        :return: The is_playable of this ChapterBase.  # noqa: E501
        :rtype: bool
        """
        return self._is_playable

    @is_playable.setter
    def is_playable(self, is_playable):
        """Sets the is_playable of this ChapterBase.

        True if the episode is playable in the given market. Otherwise false.   # noqa: E501

        :param is_playable: The is_playable of this ChapterBase.  # noqa: E501
        :type: bool
        """
        if is_playable is None:
            raise ValueError("Invalid value for `is_playable`, must not be `None`")  # noqa: E501

        self._is_playable = is_playable

    @property
    def languages(self):
        """Gets the languages of this ChapterBase.  # noqa: E501

        A list of the languages used in the episode, identified by their [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639) code.   # noqa: E501

        :return: The languages of this ChapterBase.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ChapterBase.

        A list of the languages used in the episode, identified by their [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639) code.   # noqa: E501

        :param languages: The languages of this ChapterBase.  # noqa: E501
        :type: list[str]
        """
        if languages is None:
            raise ValueError("Invalid value for `languages`, must not be `None`")  # noqa: E501

        self._languages = languages

    @property
    def name(self):
        """Gets the name of this ChapterBase.  # noqa: E501

        The name of the episode.   # noqa: E501

        :return: The name of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChapterBase.

        The name of the episode.   # noqa: E501

        :param name: The name of this ChapterBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def release_date(self):
        """Gets the release_date of this ChapterBase.  # noqa: E501

        The date the episode was first released, for example `\"1981-12-15\"`. Depending on the precision, it might be shown as `\"1981\"` or `\"1981-12\"`.   # noqa: E501

        :return: The release_date of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this ChapterBase.

        The date the episode was first released, for example `\"1981-12-15\"`. Depending on the precision, it might be shown as `\"1981\"` or `\"1981-12\"`.   # noqa: E501

        :param release_date: The release_date of this ChapterBase.  # noqa: E501
        :type: str
        """
        if release_date is None:
            raise ValueError("Invalid value for `release_date`, must not be `None`")  # noqa: E501

        self._release_date = release_date

    @property
    def release_date_precision(self):
        """Gets the release_date_precision of this ChapterBase.  # noqa: E501

        The precision with which `release_date` value is known.   # noqa: E501

        :return: The release_date_precision of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._release_date_precision

    @release_date_precision.setter
    def release_date_precision(self, release_date_precision):
        """Sets the release_date_precision of this ChapterBase.

        The precision with which `release_date` value is known.   # noqa: E501

        :param release_date_precision: The release_date_precision of this ChapterBase.  # noqa: E501
        :type: str
        """
        if release_date_precision is None:
            raise ValueError("Invalid value for `release_date_precision`, must not be `None`")  # noqa: E501
        allowed_values = ["year", "month", "day"]  # noqa: E501
        if release_date_precision not in allowed_values:
            raise ValueError(
                "Invalid value for `release_date_precision` ({0}), must be one of {1}"  # noqa: E501
                .format(release_date_precision, allowed_values)
            )

        self._release_date_precision = release_date_precision

    @property
    def resume_point(self):
        """Gets the resume_point of this ChapterBase.  # noqa: E501

        The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'.   # noqa: E501

        :return: The resume_point of this ChapterBase.  # noqa: E501
        :rtype: AllOfChapterBaseResumePoint
        """
        return self._resume_point

    @resume_point.setter
    def resume_point(self, resume_point):
        """Sets the resume_point of this ChapterBase.

        The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'.   # noqa: E501

        :param resume_point: The resume_point of this ChapterBase.  # noqa: E501
        :type: AllOfChapterBaseResumePoint
        """
        if resume_point is None:
            raise ValueError("Invalid value for `resume_point`, must not be `None`")  # noqa: E501

        self._resume_point = resume_point

    @property
    def type(self):
        """Gets the type of this ChapterBase.  # noqa: E501

        The object type.   # noqa: E501

        :return: The type of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChapterBase.

        The object type.   # noqa: E501

        :param type: The type of this ChapterBase.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["episode"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uri(self):
        """Gets the uri of this ChapterBase.  # noqa: E501

        The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the episode.   # noqa: E501

        :return: The uri of this ChapterBase.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ChapterBase.

        The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the episode.   # noqa: E501

        :param uri: The uri of this ChapterBase.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def restrictions(self):
        """Gets the restrictions of this ChapterBase.  # noqa: E501

        Included in the response when a content restriction is applied.   # noqa: E501

        :return: The restrictions of this ChapterBase.  # noqa: E501
        :rtype: AllOfChapterBaseRestrictions
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this ChapterBase.

        Included in the response when a content restriction is applied.   # noqa: E501

        :param restrictions: The restrictions of this ChapterBase.  # noqa: E501
        :type: AllOfChapterBaseRestrictions
        """

        self._restrictions = restrictions

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
        if issubclass(ChapterBase, dict):
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
        if not isinstance(other, ChapterBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other