# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.audiobooks_api import AudiobooksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAudiobooksApi(unittest.TestCase):
    """AudiobooksApi unit test stubs"""

    def setUp(self):
        self.api = AudiobooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_users_saved_audiobooks(self):
        """Test case for check_users_saved_audiobooks

        Check User's Saved Audiobooks   # noqa: E501
        """
        pass

    def test_get_an_audiobook(self):
        """Test case for get_an_audiobook

        Get an Audiobook   # noqa: E501
        """
        pass

    def test_get_audiobook_chapters(self):
        """Test case for get_audiobook_chapters

        Get Audiobook Chapters   # noqa: E501
        """
        pass

    def test_get_multiple_audiobooks(self):
        """Test case for get_multiple_audiobooks

        Get Several Audiobooks   # noqa: E501
        """
        pass

    def test_get_users_saved_audiobooks(self):
        """Test case for get_users_saved_audiobooks

        Get User's Saved Audiobooks   # noqa: E501
        """
        pass

    def test_remove_audiobooks_user(self):
        """Test case for remove_audiobooks_user

        Remove User's Saved Audiobooks   # noqa: E501
        """
        pass

    def test_save_audiobooks_user(self):
        """Test case for save_audiobooks_user

        Save Audiobooks for Current User   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
