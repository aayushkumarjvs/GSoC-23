import json
import os

# Create the 'audiofiles' folder if it doesn't exist
if not os.path.exists('audiofiles'):
    os.makedirs('audiofiles')

# Read 'segments.txt' and process each sentence
with open('segments.txt', 'r') as segments_file:
    sentences = segments_file.readlines()

    # Create a list to store sample information
    samples = []

    # Process each sentence using a for loop
    for sentence in sentences:
        sentence = sentence.strip().split('\t')
        start_time = float(sentence[0])
        end_time = float(sentence[1])
        text = sentence[2]

        # Crop the audio file based on start and end times
        audio_file_path = 'path_to_original_audio_file.wav'  # Replace with the actual path to your audio file
        cropped_audio_path = os.path.join('audiofiles', f'{text}.wav')

        # Crop the audio file
        # Your code to crop the audio file based on start and end times goes here

        # Calculate the duration of the cropped audio
        duration = end_time - start_time

        # Store the sample information in the samples list
        sample = {
            'audiofilepath': cropped_audio_path,
            'text': text,
            'duration': duration
        }
        samples.append(sample)

# Write the sample information to 'samples.json'
with open('samples.json', 'w') as samples_file:
    json.dump(samples, samples_file, indent=4)
