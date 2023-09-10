import re

def extract_clean_sentences(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extracting individual stories from the input content
    stories = re.findall(r'Start Time: [\d:.]+\s+Content:\s+([\s\S]*?)(?=\n\n(?:Turn|Story) \d+|$)', content)

    clean_sentences = []
    for story in stories:
        # Removing the metadata lines
        lines = story.split('\n')
        clean_lines = [line for line in lines if not line.startswith(('<', '|'))]

        # Joining lines to form a single content string
        story_content = ' '.join(clean_lines)

        # Extracting sentences from the content
        word = re.findall(r'[A-Z][^.!?]*[.!?]', story_content)

        # Removing leading/trailing whitespaces and adding to the clean_sentences list
        clean_sentences.extend([sentence.strip() for sentence in sentences])

    return clean_sentences

if __name__ == '__main__':
    input_file = '/Users/aayush/Desktop/mid_eval/scripts/segments2.txt'
    output_sentences = extract_clean_sentences(input_file)

    # Printing the clean output sentences
    print("Clean Output Sentences:")
    for idx, sentence in enumerate(output_sentences, start=1):
        print(f"Sentence {idx}: {sentence}")
