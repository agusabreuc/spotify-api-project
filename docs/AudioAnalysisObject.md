# AudioAnalysisObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AudioAnalysisObjectMeta**](AudioAnalysisObjectMeta.md) |  | [optional] 
**track** | [**AudioAnalysisObjectTrack**](AudioAnalysisObjectTrack.md) |  | [optional] 
**bars** | [**list[TimeIntervalObject]**](TimeIntervalObject.md) | The time intervals of the bars throughout the track. A bar (or measure) is a segment of time defined as a given number of beats. | [optional] 
**beats** | [**list[TimeIntervalObject]**](TimeIntervalObject.md) | The time intervals of beats throughout the track. A beat is the basic time unit of a piece of music; for example, each tick of a metronome. Beats are typically multiples of tatums. | [optional] 
**sections** | [**list[SectionObject]**](SectionObject.md) | Sections are defined by large variations in rhythm or timbre, e.g. chorus, verse, bridge, guitar solo, etc. Each section contains its own descriptions of tempo, key, mode, time_signature, and loudness. | [optional] 
**segments** | [**list[SegmentObject]**](SegmentObject.md) | Each segment contains a roughly conisistent sound throughout its duration. | [optional] 
**tatums** | [**list[TimeIntervalObject]**](TimeIntervalObject.md) | A tatum represents the lowest regular pulse train that a listener intuitively infers from the timing of perceived musical events (segments). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

