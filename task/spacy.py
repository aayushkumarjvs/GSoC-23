import spacy

nlp = spacy.load('en_core_web_sm')

def parse_file_spacy(file_path):
    words_and_tags = []
    with open(file_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            doc = nlp(line)
            words_and_tags.extend([(token.text, token.pos_) for token in doc])

    return words_and_tags

# Replace 'your_file.txt' with the path to your file
result_spacy = parse_file_spacy('/Users/aayush/Desktop/task/2016-12-31_0300_US_FOX-News_Hannity.v4.vrt')

for word, tag in result_spacy:
    print(f"Word: {word}, POS: {tag}")