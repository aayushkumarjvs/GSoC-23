'''import csv
def convert_vrt_to_txt(vrt_filename, txt_filename):
    with open(vrt_filename, 'r') as vrt_file, open(txt_filename, 'w') as txt_file:
        reader = csv.reader(vrt_file, delimiter='\t')
        for row in reader:
            if len(row) < 3:
                continue  # Skip rows with not enough data
            turn_text = row[0]
            start = row[1]
            end = row[2]
            txt_file.write(f"{turn_text}\t{start}\t{end}\n")
convert_vrt_to_txt('/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt', 'output.txt')'''

import xml.etree.ElementTree as ET

def parse_vrt_file(filename):
    data = []

    tree = ET.parse(filename)
    root = tree.getroot()

    for text in root.findall('text'):
        text_data = text.attrib

        for story in text.findall('story'):
            for turn in story.findall('turn'):
                turn_data = turn.attrib

                for s in turn.findall('s'):
                    s_data = s.attrib
                    words = []

                    for word in s.findall('w'):
                        word_data = word.attrib
                        word_data['word'] = word.text
                        words.append(word_data)
                    
                    s_data['words'] = words
                    turn_data['sentences'] = s_data
                
                text_data['turns'] = turn_data

            data.append(text_data)

    return data

filename = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt'
data = parse_vrt_file(filename)
print(data)
