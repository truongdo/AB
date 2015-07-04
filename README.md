# MOS
## Introduction ##
This is a AB[x] evaluation web-based application based on web2py.

__Features list__:

1. Support multiple test sets.
2. Support multiple subjects to evaluate at the same time.
3. The audios will be played sequencially, so it should be randomized before input
to the applicatin.
4. Download the result in various formats such as CSV, JSON.
5. Support both AB and ABx evaluation.

## How to install ##
1. Download and install [web2py](http://www.web2py.com/)
2. Open web2py admin page and fill in the information as below image:
   * Name: MOS
   * Get from URL: https://github.com/truongdq54/AB.git
3. Click Install

## How to use ##
The application works as follows:

1. Input database
    * Open data mangage by click to __data__ in the top menu
    You can input the data one by one by click __Add Record__ or add all the data in batch mode by click __Batch add__.
    
    * __Batch add__:
    In __Batch add__ mode, the data format is as follow:
    ```
    utterance_name|test_set|text|audio_path_1|method_1|audio_path_2|method_2|audio_path_ref|reference
    ``` 
    __utterance_name__: is an unique name for every utterance  
    __test_set__: This is useful when you want to divide your test data  
      into small test sets. The subject can select the test set that they want to evaluate.  
    __audio_path_[1,2]__: This is the relative path of the audio for method 1 and 2, respectively.
    __method_[1,2]__: is the name for each method.
    __reference__: name of reference audio.

    For all utterance, you have to upload  
        the audio to __static/wav/__ folder. For examples, if you have the audio in `static/wav/baseline/audio1.wav`,
        then the correct audio_path is __baseline/audio1.wav__.
    
    Examples:
    ```
    utt_id1|test_set_id1|text|audiopath_baseline|baseline|audiopath_proposed|proposed|audiopath_origin|original
    utt_id2|test_set_id1|text|audiopath_baseline|baseline|audiopath_proposed|proposed|audiopath_origin|original
    utt_id3|test_set_id1|text|audiopath_proposed|proposed|audiopath_baseline|baseline|audiopath_origin|original
    utt_id4|test_set_id2|text|audiopath_baseline|baseline|audiopath_proposed|proposed|audiopath_origin|original
    utt_id5|test_set_id2|text|audiopath_proposed|proposed|audiopath_baseline|baseline|audiopath_origin|original
    utt_id6|test_set_id2|text|audiopath_baseline|baseline|audiopath_proposed|proposed|audiopath_origin|original
    utt_id7|test_set_id3|text|audiopath_baseline|baseline|audiopath_proposed|proposed|audiopath_origin|original
    ```

2. The evaluator fill in their name and age. In addition a list of registered user is also displayed in the Index page

3. Select test set to be evaluated

5. The result will be showed in __result__ page in the top menu
You can download the reuslt in many difference format such as CSV, HTML, JSON.

