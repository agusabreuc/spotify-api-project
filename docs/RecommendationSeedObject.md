# RecommendationSeedObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_filtering_size** | **int** | The number of tracks available after min\\_\\* and max\\_\\* filters have been applied.  | [optional] 
**after_relinking_size** | **int** | The number of tracks available after relinking for regional availability.  | [optional] 
**href** | **str** | A link to the full track or artist data for this seed. For tracks this will be a link to a Track Object. For artists a link to an Artist Object. For genre seeds, this value will be &#x60;null&#x60;.  | [optional] 
**id** | **str** | The id used to select this seed. This will be the same as the string used in the &#x60;seed_artists&#x60;, &#x60;seed_tracks&#x60; or &#x60;seed_genres&#x60; parameter.  | [optional] 
**initial_pool_size** | **int** | The number of recommended tracks available for this seed.  | [optional] 
**type** | **str** | The entity type of this seed. One of &#x60;artist&#x60;, &#x60;track&#x60; or &#x60;genre&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

