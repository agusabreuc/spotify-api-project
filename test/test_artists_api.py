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
from swagger_client.api.artists_api import ArtistsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestArtistsApi(unittest.TestCase):
    """ArtistsApi unit test stubs"""

    def setUp(self):
        self.api = ArtistsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_current_user_follows(self):
        """Test case for check_current_user_follows

        Check If User Follows Artists or Users   # noqa: E501
        """
        pass

    def test_follow_artists_users(self):
        """Test case for follow_artists_users

        Follow Artists or Users   # noqa: E501
        """
        pass

    def test_get_an_artist(self):
        """Test case for get_an_artist

        Get Artist   # noqa: E501
        """
        pass

    def test_get_an_artists_albums(self):
        """Test case for get_an_artists_albums

        Get Artist's Albums   # noqa: E501
        """
        pass

    def test_get_an_artists_related_artists(self):
        """Test case for get_an_artists_related_artists

        Get Artist's Related Artists   # noqa: E501
        """
        pass

    def test_get_an_artists_top_tracks(self):
        """Test case for get_an_artists_top_tracks

        Get Artist's Top Tracks   # noqa: E501
        """
        pass

    def test_get_followed(self):
        """Test case for get_followed

        Get Followed Artists   # noqa: E501
        """
        pass

    def test_get_multiple_artists(self):
        """Test case for get_multiple_artists

        Get Several Artists   # noqa: E501
        """
        pass

    def test_unfollow_artists_users(self):
        """Test case for unfollow_artists_users

        Unfollow Artists or Users   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()