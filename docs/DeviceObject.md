# DeviceObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The device ID. | [optional] 
**is_active** | **bool** | If this device is the currently active device. | [optional] 
**is_private_session** | **bool** | If this device is currently in a private session. | [optional] 
**is_restricted** | **bool** | Whether controlling this device is restricted. At present if this is \&quot;true\&quot; then no Web API commands will be accepted by this device. | [optional] 
**name** | **str** | A human-readable name for the device. Some devices have a name that the user can configure (e.g. \\\&quot;Loudest speaker\\\&quot;) and some devices have a generic name associated with the manufacturer or device model. | [optional] 
**type** | **str** | Device type, such as \&quot;computer\&quot;, \&quot;smartphone\&quot; or \&quot;speaker\&quot;. | [optional] 
**volume_percent** | **int** | The current volume in percent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

