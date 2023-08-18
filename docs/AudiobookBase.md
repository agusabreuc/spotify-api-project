# AudiobookBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authors** | [**list[AuthorObject]**](AuthorObject.md) | The author(s) for the audiobook.  | 
**available_markets** | **list[str]** | A list of the countries in which the audiobook can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.  | 
**copyrights** | [**list[CopyrightObject]**](CopyrightObject.md) | The copyright statements of the audiobook.  | 
**description** | **str** | A description of the audiobook. HTML tags are stripped away from this field, use &#x60;html_description&#x60; field in case HTML tags are needed.  | 
**html_description** | **str** | A description of the audiobook. This field may contain HTML tags.  | 
**edition** | **str** | The edition of the audiobook.  | [optional] 
**explicit** | **bool** | Whether or not the audiobook has explicit content (true &#x3D; yes it does; false &#x3D; no it does not OR unknown).  | 
**external_urls** | **AllOfAudiobookBaseExternalUrls** | External URLs for this audiobook.  | 
**href** | **str** | A link to the Web API endpoint providing full details of the audiobook.  | 
**id** | **str** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook.  | 
**images** | [**list[ImageObject]**](ImageObject.md) | The cover art for the audiobook in various sizes, widest first.  | 
**languages** | **list[str]** | A list of the languages used in the audiobook, identified by their [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code.  | 
**media_type** | **str** | The media type of the audiobook.  | 
**name** | **str** | The name of the audiobook.  | 
**narrators** | [**list[NarratorObject]**](NarratorObject.md) | The narrator(s) for the audiobook.  | 
**publisher** | **str** | The publisher of the audiobook.  | 
**type** | **str** | The object type.  | 
**uri** | **str** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the audiobook.  | 
**total_chapters** | **int** | The number of chapters in this audiobook.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

