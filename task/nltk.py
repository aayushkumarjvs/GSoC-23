import nltk

# Function to parse the file and return the words
def parse_file(filename):
    words = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            word, pos = line.strip().split(" ")
            words.append(word)
    return words

filename = '/Users/aayush/Desktop/task/2016-12-31_0300_US_FOX-News_Hannity.v4.vrt'
words = parse_file(filename)
print(words)
