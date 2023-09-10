import re

def parse_text_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            # Extract sentence number
            sentence_number = re.search(r"Sentence (\d+)", line)
            sentence_number = sentence_number.group(1) if sentence_number else ""

            # Extract sentence content
            sentence_content = re.search(r"Sentence \d+: (.*?)(?=\|)", line)
            sentence_content = sentence_content.group(1).strip() if sentence_content else ""

            # Extract start and end times
            start_time = re.search(r"\|\s+(\d+:\d+:\d+)\s+\|", line)
            start_time = start_time.group(1) if start_time else ""

            end_time = re.search(r"\|\s+\d+:\d+:\d+\s+\|\s+(\d+:\d+:\d+)", line)
            end_time = end_time.group(1) if end_time else ""

            print(f"Sentence {sentence_number} : {sentence_content} | {start_time} | {end_time}")

parse_text_file('/Users/aayush/Desktop/mid_eval/scripts/segments3.txt')
