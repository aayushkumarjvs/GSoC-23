import os
import pandas as pd
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

# Function to create 'segments.txt'
def create_segments(vrt_file):
    try:
        df = pd.read_csv(vrt_file, sep='\t', header=None)
        df.to_csv('segments.txt', sep='\t', index=False, header=False)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

# Function to extract audio from video
def extract_audio(video_file):
    try:
        clip = VideoFileClip(video_file)
        clip.audio.write_audiofile("audio.mp3")
    except Exception as e:
        print(f"An error occurred: {e}")
        return

# Function to segment audio file and generate samples.json
def process_segments():
    try:
        audio = AudioSegment.from_mp3("audio.mp3")
        df = pd.read_csv('segments.txt', sep='\t', header=None)
        samples = []
        for i, row in df.iterrows():
            start = int(row[1]*1000)
            end = int(row[2]*1000)
            segment = audio[start:end]
            segment.export(f"audiofiles/audio{i}.mp3", format="mp3")
            samples.append({"audiofilepath": f"audiofiles/audio{i}.mp3", "text": row[0], "duration": row[2] - row[1]})

        with open("samples.json", "w") as f:
            json.dump(samples, f)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

# Main function
def main():
    # Check if ffmpeg is installed
    if os.system('ffmpeg -version') != 0:
        print("ffmpeg not found. Please install it and add to PATH.")
        return

    vrt_file = "/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt"
    video_file = "/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_OutFront.mp4"

    create_segments(vrt_file)
    extract_audio(video_file)
    process_segments()

if __name__ == '__main__':
    main()
