# AudioAnalysisObjectTrack

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_samples** | **int** | The exact number of audio samples analyzed from this track. See also &#x60;analysis_sample_rate&#x60;. | [optional] 
**duration** | **float** | Length of the track in seconds. | [optional] 
**sample_md5** | **str** | This field will always contain the empty string. | [optional] 
**offset_seconds** | **int** | An offset to the start of the region of the track that was analyzed. (As the entire track is analyzed, this should always be 0.) | [optional] 
**window_seconds** | **int** | The length of the region of the track was analyzed, if a subset of the track was analyzed. (As the entire track is analyzed, this should always be 0.) | [optional] 
**analysis_sample_rate** | **int** | The sample rate used to decode and analyze this track. May differ from the actual sample rate of this track available on Spotify. | [optional] 
**analysis_channels** | **int** | The number of channels used for analysis. If 1, all channels are summed together to mono before analysis. | [optional] 
**end_of_fade_in** | **float** | The time, in seconds, at which the track&#x27;s fade-in period ends. If the track has no fade-in, this will be 0.0. | [optional] 
**start_of_fade_out** | **float** | The time, in seconds, at which the track&#x27;s fade-out period starts. If the track has no fade-out, this should match the track&#x27;s length. | [optional] 
**loudness** | [**Loudness**](Loudness.md) |  | [optional] 
**tempo** | [**Tempo**](Tempo.md) |  | [optional] 
**tempo_confidence** | **float** | The confidence, from 0.0 to 1.0, of the reliability of the &#x60;tempo&#x60;. | [optional] 
**time_signature** | [**TimeSignature**](TimeSignature.md) |  | [optional] 
**time_signature_confidence** | **float** | The confidence, from 0.0 to 1.0, of the reliability of the &#x60;time_signature&#x60;. | [optional] 
**key** | [**Key**](Key.md) |  | [optional] 
**key_confidence** | **float** | The confidence, from 0.0 to 1.0, of the reliability of the &#x60;key&#x60;. | [optional] 
**mode** | [**Mode**](Mode.md) |  | [optional] 
**mode_confidence** | **float** | The confidence, from 0.0 to 1.0, of the reliability of the &#x60;mode&#x60;. | [optional] 
**codestring** | **str** | An [Echo Nest Musical Fingerprint (ENMFP)](https://academiccommons.columbia.edu/doi/10.7916/D8Q248M4) codestring for this track. | [optional] 
**code_version** | **float** | A version number for the Echo Nest Musical Fingerprint format used in the codestring field. | [optional] 
**echoprintstring** | **str** | An [EchoPrint](https://github.com/spotify/echoprint-codegen) codestring for this track. | [optional] 
**echoprint_version** | **float** | A version number for the EchoPrint format used in the echoprintstring field. | [optional] 
**synchstring** | **str** | A [Synchstring](https://github.com/echonest/synchdata) for this track. | [optional] 
**synch_version** | **float** | A version number for the Synchstring used in the synchstring field. | [optional] 
**rhythmstring** | **str** | A Rhythmstring for this track. The format of this string is similar to the Synchstring. | [optional] 
**rhythm_version** | **float** | A version number for the Rhythmstring used in the rhythmstring field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

