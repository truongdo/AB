# MOS
## Introduction ##
This is a mean opinion score (MOS) evaluation web-based application based on web2py.

__Features list__:

1. Support multiple test sets.
2. Support multiple subjects to evaluate at the same time.
3. The audios will be played sequencially, so it should be randomized before input
to the applicatin.
4. Download the result in various formats such as CSV, JSON.

## How to install ##
1. Download and install [web2py](http://www.web2py.com/)
2. Open web2py admin page and fill in the information as below image:
   * Name: MOS
   * Get from URL: https://github.com/truongdq54/MOS.git
3. Click Install

![Install](https://lh3.googleusercontent.com/TWR6Dzb1bwZCpnZIiDXPIQVaaLQSla3502Ki7Jafq2k=w472-h347-no "Install")

## How to use ##
The application works as follows:

1. Input database
    * Open data mangage by click to __data__ in the top menu
   ![Open data manage](https://lh3.googleusercontent.com/01fysed7Aeu6YPc8KlVsiC9R6zFrQZlVpwtJrvpdIHA=w950-h493-no)
    You can input the data one by one by click __Add Record__ or add all the data in batch mode by click __Batch add__.
    
    * __Batch add__:
    In __Batch add__ mode, the data format is as follow:
    ```
    utterance_name|test_set|text|audio_path|system
    ``` 
    __utterance_name__: is an unique name for every utterance  
    __test_set__: This is useful when you want to divide your test data  
      into small test sets. The subject can select the test set that they want to evaluate.  
    __audio_path__: This is the relative path of the audio. For all utterance, you have to upload  
        the audio to __static/wav/__ folder. For examples, if you have the audio in `static/wav/baseline/audio1.wav`,
        then the correct audio_path is __baseline/audio1.wav__.


    Examples:
    ![pic alt](https://lh3.googleusercontent.com/6CddbSUuj5H0f4He9sFiUy7_T-zXw_VJk_TVkgibqxA=w950-h629-no "opt title")

2. The evaluator fill in their name and age. In addition a list of registered user is also displayed in the Index page
![pic alt](https://lh3.googleusercontent.com/HZLU9CqtcM-tlz2iQ-Eb9u4blYnIDbYvoQBYQKBbna0=w925-h550-no "opt title")

3. Select test set to be evaluated
![pic alt](https://lh3.googleusercontent.com/-o28oL84slPjHivHHUBqqHHpxcOwJsrv0I2U5WL47qA=w950-h452-no "opt title")

4. The evaluation page looks like below:
![pic alt](https://lh3.googleusercontent.com/6AfAFUiVpde3RiHVgnAAtun0fmJa0nYCIZFo9WeeBgo=w950-h560-no "opt title")
User select the score for each utterance and click submit.

5. The result will be showed in __result__ page in the top menu:
![pic alt](https://lh3.googleusercontent.com/keWLJvmAsX7g4l1VTiXB48yAuyxG0jYzJxVreyFpsgQ=w950-h433-no "opt title")
You can download the reuslt in many difference format such as CSV, HTML, JSON.

