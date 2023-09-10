def extract_clean_sentences(input_file):
    sentences = []
    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()
        paragraphs = data.split('</s>')
        for paragraph in paragraphs:
            sentence_lines = paragraph.strip().split('\n')
            if sentence_lines and len(sentence_lines[0].split('\t')) >= 2:
                sentence = ' '.join(line.split('\t')[1] for line in sentence_lines)
                sentences.append(sentence)
    return sentences


def save_segments_to_file(sentences, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(f'{sentence} <TAB> start_time\n')


if __name__ == "__main__":
    input_file = "/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt"   # Replace with the actual path to your VRT file
    output_file = "segments4.txt"

    try:
        clean_sentences = extract_clean_sentences(input_file)
        save_segments_to_file(clean_sentences, output_file)
        print("Segments have been successfully saved to segments4.txt.")
    except Exception as e:
        print(f"Error: {e}")

