import random
from datetime import datetime, timedelta

def read_file_and_process(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        results = []
        for i, line in enumerate(lines):
            line = line.strip()  # remove extra whitespace and newline characters
            start_time, end_time = generate_random_time_stamps()  # generate random timestamps
            
            # Split the line into two parts, the 'Sentence X' part and the 'Content' part
            sentence_prefix, content = line.split(':', 1)

            # Add back the ':' to the content part and remove extra spaces
            content = content.strip()

            # Create the final formatted string and add it to the results list
            results.append(f"{sentence_prefix} : {content} : {start_time} : {end_time}")

        return results

def generate_random_time_stamps():
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)

    start_time = datetime.now().replace(hour=random_hours, minute=random_minutes, second=random_seconds)

    # end_time is assumed to be within the same hour and the duration is a random number of minutes and seconds
    random_end_minutes = random.randint(0, 59)
    random_end_seconds = random.randint(0, 59)
    end_time = start_time + timedelta(minutes=random_end_minutes, seconds=random_end_seconds)
    
    return start_time.strftime("%H:%M:%S"), end_time.strftime("%H:%M:%S")

file_path = "/Users/aayush/Desktop/mid_eval/scripts/segments3.txt"  # replace with your file path
results = read_file_and_process(file_path)
for result in results:
    print(result)


# parse_file('/Users/aayush/Desktop/mid_eval/scripts/segments3.txt', 'output.txt')
