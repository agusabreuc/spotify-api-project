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

class AudioAnalysisObjectMeta(object):
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
        'analyzer_version': 'str',
        'platform': 'str',
        'detailed_status': 'str',
        'status_code': 'int',
        'timestamp': 'int',
        'analysis_time': 'float',
        'input_process': 'str'
    }

    attribute_map = {
        'analyzer_version': 'analyzer_version',
        'platform': 'platform',
        'detailed_status': 'detailed_status',
        'status_code': 'status_code',
        'timestamp': 'timestamp',
        'analysis_time': 'analysis_time',
        'input_process': 'input_process'
    }

    def __init__(self, analyzer_version=None, platform=None, detailed_status=None, status_code=None, timestamp=None, analysis_time=None, input_process=None):  # noqa: E501
        """AudioAnalysisObjectMeta - a model defined in Swagger"""  # noqa: E501
        self._analyzer_version = None
        self._platform = None
        self._detailed_status = None
        self._status_code = None
        self._timestamp = None
        self._analysis_time = None
        self._input_process = None
        self.discriminator = None
        if analyzer_version is not None:
            self.analyzer_version = analyzer_version
        if platform is not None:
            self.platform = platform
        if detailed_status is not None:
            self.detailed_status = detailed_status
        if status_code is not None:
            self.status_code = status_code
        if timestamp is not None:
            self.timestamp = timestamp
        if analysis_time is not None:
            self.analysis_time = analysis_time
        if input_process is not None:
            self.input_process = input_process

    @property
    def analyzer_version(self):
        """Gets the analyzer_version of this AudioAnalysisObjectMeta.  # noqa: E501

        The version of the Analyzer used to analyze this track.  # noqa: E501

        :return: The analyzer_version of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._analyzer_version

    @analyzer_version.setter
    def analyzer_version(self, analyzer_version):
        """Sets the analyzer_version of this AudioAnalysisObjectMeta.

        The version of the Analyzer used to analyze this track.  # noqa: E501

        :param analyzer_version: The analyzer_version of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: str
        """

        self._analyzer_version = analyzer_version

    @property
    def platform(self):
        """Gets the platform of this AudioAnalysisObjectMeta.  # noqa: E501

        The platform used to read the track's audio data.  # noqa: E501

        :return: The platform of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this AudioAnalysisObjectMeta.

        The platform used to read the track's audio data.  # noqa: E501

        :param platform: The platform of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def detailed_status(self):
        """Gets the detailed_status of this AudioAnalysisObjectMeta.  # noqa: E501

        A detailed status code for this track. If analysis data is missing, this code may explain why.  # noqa: E501

        :return: The detailed_status of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._detailed_status

    @detailed_status.setter
    def detailed_status(self, detailed_status):
        """Sets the detailed_status of this AudioAnalysisObjectMeta.

        A detailed status code for this track. If analysis data is missing, this code may explain why.  # noqa: E501

        :param detailed_status: The detailed_status of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: str
        """

        self._detailed_status = detailed_status

    @property
    def status_code(self):
        """Gets the status_code of this AudioAnalysisObjectMeta.  # noqa: E501

        The return code of the analyzer process. 0 if successful, 1 if any errors occurred.  # noqa: E501

        :return: The status_code of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this AudioAnalysisObjectMeta.

        The return code of the analyzer process. 0 if successful, 1 if any errors occurred.  # noqa: E501

        :param status_code: The status_code of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def timestamp(self):
        """Gets the timestamp of this AudioAnalysisObjectMeta.  # noqa: E501

        The Unix timestamp (in seconds) at which this track was analyzed.  # noqa: E501

        :return: The timestamp of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AudioAnalysisObjectMeta.

        The Unix timestamp (in seconds) at which this track was analyzed.  # noqa: E501

        :param timestamp: The timestamp of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def analysis_time(self):
        """Gets the analysis_time of this AudioAnalysisObjectMeta.  # noqa: E501

        The amount of time taken to analyze this track.  # noqa: E501

        :return: The analysis_time of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: float
        """
        return self._analysis_time

    @analysis_time.setter
    def analysis_time(self, analysis_time):
        """Sets the analysis_time of this AudioAnalysisObjectMeta.

        The amount of time taken to analyze this track.  # noqa: E501

        :param analysis_time: The analysis_time of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: float
        """

        self._analysis_time = analysis_time

    @property
    def input_process(self):
        """Gets the input_process of this AudioAnalysisObjectMeta.  # noqa: E501

        The method used to read the track's audio data.  # noqa: E501

        :return: The input_process of this AudioAnalysisObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._input_process

    @input_process.setter
    def input_process(self, input_process):
        """Sets the input_process of this AudioAnalysisObjectMeta.

        The method used to read the track's audio data.  # noqa: E501

        :param input_process: The input_process of this AudioAnalysisObjectMeta.  # noqa: E501
        :type: str
        """

        self._input_process = input_process

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
        if issubclass(AudioAnalysisObjectMeta, dict):
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
        if not isinstance(other, AudioAnalysisObjectMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other