import re

def extract_turns(vrt_content):
    pattern = r'<s id="[^"]+" file="[^"]+" starttime="([^"]+)" reltime="\d+">\n([^<]+)\n<\/s>'
    turns = re.findall(pattern, vrt_content)
    return turns

def clean_text(text):
    # Remove any remaining XML tags and leading/trailing whitespaces
    cleaned_text = re.sub(r'<[^>]+>', '', text).strip()
    return cleaned_text

def process_vrt_file(file_path):
    with open(file_path, 'r') as file:
        vrt_content = file.read()

    turns = extract_turns(vrt_content)

    if not turns:
        print("No turns found in the VRT file.")
        return

    for i, (start_time, turn_content) in enumerate(turns, start=1):
        processed_text = clean_text(turn_content)

        print(f"Turn {i}:")
        print(f"Start Time: {start_time}")
        print("Content:")
        print(processed_text)
        print()

# Usage
vrt_file_path = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt'
process_vrt_file(vrt_file_path)
