import os
import subprocess

# Input files
vrt_file = "/Users/aayush/Desktop/task/2016-12-31_0300_US_FOX-News_Hannity.v4.vrt"
video_file = "/Users/aayush/Desktop/task/2016-12-31_0300_US_FOX-News_Hannity.mp4"

# Output files
segments_file = "segments.txt"
audio_folder = "audiofiles"
samples_file = "samples.json"

# Ensure the audio_folder exists
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Create segments.txt file from VRT file
with open(vrt_file, "r") as f:
    lines = f.readlines()

# Remove comments and empty lines
lines = [line for line in lines if not line.startswith("#") and len(line.strip()) > 0]

# Extract turn numbers and text
turns = []
for line in lines:
    parts = line.split(" ")
    if parts[0].startswith("turn") and parts[0][4:].isdigit():
        turn = int(parts[0][4:])
        text = ' '.join(parts[1:])
        turns.append((turn, text))
    else:
        print(f"Skipping line: {line}")

# Write segments.txt file
with open(segments_file, "w") as f:
    for turn, text in turns:
        f.write(f"{turn}-text {text}\n")

# Initialize audio file counter
audio_counter = 0

samples = []

# Loop through each segment
for turn, text in turns:
    # Get the start and end times for the current segment
    start = float(text.split(" ")[0])
    end = float(text.split(" ")[1])

    # Crop the audio file for the current segment
    audio_file = os.path.join(audio_folder, f"segment_{audio_counter}.mp3")
    subprocess.run(["ffmpeg", "-i", video_file, "-ss", str(start), "-to", str(end), "-c:a", "copy", audio_file])

    # Get the duration
    cmd_output = subprocess.check_output(["ffprobe", "-i", audio_file, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]).decode()
    duration = float(cmd_output.strip())

    samples.append({
        "audiofilepath": audio_file,
        "text": ' '.join(text.split(" ")[2:]),
        "duration": duration
    })

    # Increment the audio file counter
    audio_counter += 1

# Create samples.json file
with open(samples_file, "w") as f:
    json.dump(samples, f, indent=4)
