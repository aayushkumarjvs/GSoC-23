import re

def extract_story(vrt_content):
    pattern = r'<s[^>]*>(.*?)<\/s>'
    stories = re.findall(pattern, vrt_content, re.DOTALL)
    return stories

def extract_words(story):
    # pattern = r'<w[^>]*>(.*?)<\/w>'
    story = story.split('\n') 
    for s in story:
        print(s)
    # words = re.findall(pattern, story)
    return {}


def clean_text(text):
    # Remove any remaining XML tags and leading/trailing whitespaces
    cleaned_text = re.sub(r'<[^>]+>', '', text).strip()
    return cleaned_text

def process_vrt_file(file_path):
    with open(file_path, 'r') as file:
        vrt_content = file.read()
    
    stories = extract_story(vrt_content)
    # print(stories[0])
    for i, story in enumerate(stories, start=1):
        # print(f"Story {i}:")
        words = extract_words(story)
        cleaned_words = [clean_text(word) for word in words]
        processed_text = ' '.join(cleaned_words)
        
        # print(f"Story {i}:")
        # print(processed_text)
        # print()

# Usage
vrt_file_path = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt'
process_vrt_file(vrt_file_path)
