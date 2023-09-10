# GSoC-23
Project done in the summer of 2023 as part of Google Summer of Code with the organization Red Hen Labs

# Task
Made an Audio Tagging system for Red Hen Lab Inc. Wrote a script which takes - 
1. Input: 1 VRT file, 1 video file 
Process: From VRT file create "segments.txt".  This txt file has sentences with the following information. 
Turn1-Text (col1) TAB start TAB end
Turn2-Text (col1) TAB start TAB end 
2. Reading  ''segments.txt'' and then reading each sentence using a FOR loop. 
a) crop audio-file (extracted from videofile) according to start and end of sentence and store them in "audiofiles" folder. 
b) created 'samples.json' where each line has values from three keys: audiofilepath, text, duration Output segments.txt Folder with audiofiles samples.json
3. Used these samples.json in an End-to-End Automatic Speech Recognition (E2E ASR) software for Tagging/Transcribe events in Audio/Video segments.
