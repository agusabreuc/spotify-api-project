# AudioAnalysisObjectMeta

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzer_version** | **str** | The version of the Analyzer used to analyze this track. | [optional] 
**platform** | **str** | The platform used to read the track&#x27;s audio data. | [optional] 
**detailed_status** | **str** | A detailed status code for this track. If analysis data is missing, this code may explain why. | [optional] 
**status_code** | **int** | The return code of the analyzer process. 0 if successful, 1 if any errors occurred. | [optional] 
**timestamp** | **int** | The Unix timestamp (in seconds) at which this track was analyzed. | [optional] 
**analysis_time** | **float** | The amount of time taken to analyze this track. | [optional] 
**input_process** | **str** | The method used to read the track&#x27;s audio data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

