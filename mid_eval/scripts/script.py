import os
import json
import subprocess
from pydub.utils import mediainfo

def vrt_to_segments(vrt_file, txt_file):
    # Parsing VRT file to extract segments with timestamps
    # Placeholder implementation as the VRT file structure is not provided
    with open(vrt_file, 'r') as vrt, open(txt_file, 'w') as seg:
        for line in vrt:
            # Assuming each line in the VRT file is in format 'turn-text TAB start TAB end'
            seg.write(line)

def extract_audio(video_file, audio_file):
    # Using ffmpeg to extract audio from video
    command = f"ffmpeg -i {video_file} -vn -acodec pcm_s16le -ar 44100 -ac 1 {audio_file}"
    subprocess.call(command, shell=True)

def crop_audio(txt_file, audio_file, output_folder):
    # Create audiofiles directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    samples = []
    with open(txt_file, 'r') as seg:
        for line in seg:
            segment, start, end = line.strip().split('\t')
            
            # Output file for each segment
            output_audio = os.path.join(output_folder, f"{segment.replace(' ', '_')}.wav")
            
            # Crop the audio file according to start and end timestamps
            command = f"ffmpeg -ss {start} -to {end} -i {audio_file} -acodec copy {output_audio}"
            subprocess.call(command, shell=True)
            
            # Get the duration of the cropped audio
            duration = float(mediainfo(output_audio)["duration"])
            
            # Add the details to samples list
            samples.append({
                "audiofilepath": output_audio,
                "text": segment,
                "duration": duration
            })
    
    return samples

def write_samples_to_json(samples, json_file):
    with open(json_file, 'w') as jf:
        for sample in samples:
            jf.write(json.dumps(sample) + '\n')


# Main execution
vrt_file = "/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt"
video_file = "/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_OutFront.mp4"
txt_file = "segments1.txt"
audio_file = "audio.wav"
output_folder = "audiofiles"
json_file = "samples.json"

vrt_to_segments(vrt_file, txt_file)
extract_audio(video_file, audio_file)
samples = crop_audio(txt_file, audio_file, output_folder)
write_samples_to_json(samples, json_file)
