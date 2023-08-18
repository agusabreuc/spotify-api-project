# coding: utf-8

"""
    Spotify Web API

    You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AudiobooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_users_saved_audiobooks(self, ids, **kwargs):  # noqa: E501
        """Check User's Saved Audiobooks   # noqa: E501

        Check if one or more audiobooks are already saved in the current Spotify user's library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_users_saved_audiobooks(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :return: list[bool]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_users_saved_audiobooks_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.check_users_saved_audiobooks_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def check_users_saved_audiobooks_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Check User's Saved Audiobooks   # noqa: E501

        Check if one or more audiobooks are already saved in the current Spotify user's library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_users_saved_audiobooks_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :return: list[bool]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_users_saved_audiobooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `check_users_saved_audiobooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/me/audiobooks/contains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[bool]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_an_audiobook(self, id, **kwargs):  # noqa: E501
        """Get an Audiobook   # noqa: E501

        Get Spotify catalog information for a single audiobook.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.**   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_an_audiobook(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str market:
        :return: AudiobookObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_an_audiobook_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_an_audiobook_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_an_audiobook_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get an Audiobook   # noqa: E501

        Get Spotify catalog information for a single audiobook.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.**   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_an_audiobook_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str market:
        :return: AudiobookObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'market']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_an_audiobook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_an_audiobook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/audiobooks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AudiobookObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audiobook_chapters(self, id, **kwargs):  # noqa: E501
        """Get Audiobook Chapters   # noqa: E501

        Get Spotify catalog information about an audiobook's chapters.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.**   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audiobook_chapters(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str market:
        :param int limit:
        :param int offset:
        :return: PagingSimplifiedChapterObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audiobook_chapters_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audiobook_chapters_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_audiobook_chapters_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Audiobook Chapters   # noqa: E501

        Get Spotify catalog information about an audiobook's chapters.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.**   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audiobook_chapters_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str market:
        :param int limit:
        :param int offset:
        :return: PagingSimplifiedChapterObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'market', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audiobook_chapters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_audiobook_chapters`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/audiobooks/{id}/chapters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagingSimplifiedChapterObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_multiple_audiobooks(self, ids, **kwargs):  # noqa: E501
        """Get Several Audiobooks   # noqa: E501

        Get Spotify catalog information for several audiobooks identified by their Spotify IDs.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.**   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_multiple_audiobooks(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :param str market:
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_multiple_audiobooks_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_multiple_audiobooks_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def get_multiple_audiobooks_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Get Several Audiobooks   # noqa: E501

        Get Spotify catalog information for several audiobooks identified by their Spotify IDs.<br /> **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.**   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_multiple_audiobooks_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :param str market:
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids', 'market']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_multiple_audiobooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `get_multiple_audiobooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/audiobooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_users_saved_audiobooks(self, **kwargs):  # noqa: E501
        """Get User's Saved Audiobooks   # noqa: E501

        Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_saved_audiobooks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :return: PagingSimplifiedAudiobookObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_users_saved_audiobooks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_users_saved_audiobooks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_users_saved_audiobooks_with_http_info(self, **kwargs):  # noqa: E501
        """Get User's Saved Audiobooks   # noqa: E501

        Get a list of the audiobooks saved in the current Spotify user's 'Your Music' library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_users_saved_audiobooks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit:
        :param int offset:
        :return: PagingSimplifiedAudiobookObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_saved_audiobooks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/me/audiobooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagingSimplifiedAudiobookObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_audiobooks_user(self, ids, **kwargs):  # noqa: E501
        """Remove User's Saved Audiobooks   # noqa: E501

        Remove one or more audiobooks from the Spotify user's library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_audiobooks_user(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_audiobooks_user_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_audiobooks_user_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def remove_audiobooks_user_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Remove User's Saved Audiobooks   # noqa: E501

        Remove one or more audiobooks from the Spotify user's library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_audiobooks_user_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_audiobooks_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `remove_audiobooks_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/me/audiobooks', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_audiobooks_user(self, ids, **kwargs):  # noqa: E501
        """Save Audiobooks for Current User   # noqa: E501

        Save one or more audiobooks to the current Spotify user's library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_audiobooks_user(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_audiobooks_user_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.save_audiobooks_user_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def save_audiobooks_user_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Save Audiobooks for Current User   # noqa: E501

        Save one or more audiobooks to the current Spotify user's library.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_audiobooks_user_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ids: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_audiobooks_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `save_audiobooks_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth_2_0']  # noqa: E501

        return self.api_client.call_api(
            '/me/audiobooks', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)