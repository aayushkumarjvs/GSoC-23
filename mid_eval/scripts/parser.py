def parse_vrt_file(vrt_file_path):
    parsed_data = []
    
    with open(vrt_file_path, 'r') as f:
        lines = f.readlines()
        turn_data = []
        turn_name = None

        for line in lines:
            line = line.strip()
            if line:
                if line.startswith('turn'):
                    # process previous turn data
                    if turn_name and turn_data:
                        parsed_data.append((turn_name, turn_data))
                    # start new turn data
                    turn_name = line.split('\t')[0]
                    turn_data = []
                else:
                    # collect word data
                    turn_data.append(line)
        # don't forget the last turn
        if turn_name and turn_data:
            parsed_data.append((turn_name, turn_data))

    return parsed_data

def create_segments_txt(parsed_data, output_file_path):
    with open(output_file_path, 'w') as f:
        for turn_name, turn_data in parsed_data:
            f.write(f'{turn_name}\t{", ".join(turn_data)}\n')

def main():
    vrt_file_path = '/Users/aayush/Desktop/mid_eval/2016-01-01_0000_US_CNN_Erin_Burnett_Out_Front.v4.vrt'  # replace with your VRT file path
    output_file_path = 'segments.txt'  # replace with your desired output path

    parsed_data = parse_vrt_file(vrt_file_path)
    create_segments_txt(parsed_data, output_file_path)

if __name__ == "__main__":
    main()
