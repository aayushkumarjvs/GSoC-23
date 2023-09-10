import pandas as pd
import os
import json
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

# Change these as needed
VRT_FILE_PATH = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt'
VIDEO_FILE_PATH = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_OutFront.mp4'
AUDIO_FOLDER_PATH = '/Users/aayush/Desktop/mid_eval/'
JSON_FILE_PATH = '/Users/aayush/Desktop/mid_eval/samples.json'

def main():
    # Check if ffmpeg is installed
    if os.system('ffmpeg -version') != 0:
    print("ffmpeg not found. Please install it and add to PATH.")
    return

    # Check if file paths are valid
    if not os.path.isfile(VRT_FILE_PATH):
        print(f"VRT file not found: {VRT_FILE_PATH}")
        return
    if not os.path.isfile(VIDEO_FILE_PATH):
        print(f"Video file not found: {VIDEO_FILE_PATH}")
        return

    try:
        vrt_data = pd.read_csv(VRT_FILE_PATH, sep="\t", header=None)
    except pd.errors.ParserError as e:
        print(f"Error while reading VRT file: {e}")
        return

    vrt_data.columns = ["text", "start", "end"]
    vrt_data.to_csv('segments.txt', sep='\t', index=False)

    try:
        clip = VideoFileClip(VIDEO_FILE_PATH)
        clip.audio.write_audiofile("audio.mp3")
    except Exception as e:
        print(f"Error while processing video file: {e}")
        return

    audio = AudioSegment.from_mp3("audio.mp3")

    samples = []

    for index, row in vrt_data.iterrows():
        try:
            start_time = int(float(row['start']) * 1000)  # pydub works in milliseconds
            end_time = int(float(row['end']) * 1000)
            segment_audio = audio[start_time:end_time]
            filename = AUDIO_FOLDER_PATH + f"audio_{index}.mp3"
            segment_audio.export(filename, format="mp3")

            # Append the information to samples
            sample_info = {
                'audiofilepath': filename,
                'text': row['text'],
                'duration': row['end'] - row['start']
            }
            samples.append(sample_info)
        except Exception as e:
            print(f"Error while processing row {index}: {e}")

    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(samples, json_file)

if __name__ == '__main__':
    main()
