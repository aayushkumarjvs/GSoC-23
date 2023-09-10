from bs4 import BeautifulSoup

def process_vrt_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    soup = BeautifulSoup(data, 'xml')

    for turn in soup.find_all('turn'):
        sentences = turn.find_all('s')
        for sentence in sentences:
            words = []
            for word in sentence.find_all(True, recursive=False):  # direct children only
                if word.name not in ["meta", "Unknown"]:  # not interested in these tags
                    words.append(word.text)
            sentence_text = " ".join(words)
            print(sentence_text)

# Use the function
process_vrt_file('/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt')
