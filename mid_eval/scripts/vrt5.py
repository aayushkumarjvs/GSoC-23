import re

def read_vrt_file(file_path):
  with open(file_path, "r") as f:
    text = f.read()
  sentences = re.findall(r"<s id=\"(.*?)\">(.*?)</s>(.*?)(.*?)", text, re.DOTALL)
  for id, words, start_time, end_time in sentences:
    yield id, words, start_time, end_time

def main():
  file_path = "/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt"
  for id, words, start_time, end_time in read_vrt_file(file_path):
    print(f"{id} {' '.join(words)} {start_time} {end_time}")

if __name__ == "__main__":
  main()
