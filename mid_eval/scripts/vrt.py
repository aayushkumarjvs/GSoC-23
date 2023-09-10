from bs4 import BeautifulSoup
import uuid

def process_vrt_file(vrt_file_path):
    with open(vrt_file_path, "r") as f:
        content = f.read()

    bs_content = BeautifulSoup(content, "lxml")

    segments = []
    turns = bs_content.find_all('turn')
    print(f"Found {len(turns)} 'turn' tags")
    
    for turn in turns:
        turn_id = turn.get('id', str(uuid.uuid4()))  # If 'id' doesn't exist, generate a unique id
        timelines = turn.find_all('timeline')
        print(f"Found {len(timelines)} 'timeline' tags in turn {turn_id}")
        
        for timeline in timelines:
            syncs = timeline.find_all('sync')
            print(f"Found {len(syncs)} 'sync' tags in timeline")
            
            for i in range(len(syncs)-1):
                start = syncs[i]['time']
                end = syncs[i+1]['time']
                segments_between_syncs = [segment.text for segment in syncs[i].find_all_next('segment') if segment.find_next('sync') == syncs[i+1]]
                print(f"Found {len(segments_between_syncs)} 'segment' tags between sync {i} and {i+1}")
                text = ' '.join(segments_between_syncs)
                segments.append((turn_id, text, start, end))
    
    return segments

def main():
    vrt_file_path = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt'  # change this to your file path
    segments = process_vrt_file(vrt_file_path)

    with open('segments.txt', 'w') as f:
        for seg in segments:
            f.write(f"{seg[0]}-{seg[1]}\t{seg[2]}\t{seg[3]}\n")

if __name__ == "__main__":
    main()
