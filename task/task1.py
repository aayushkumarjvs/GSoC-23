# Open the VRT file and read its contents
with open('/Users/aayush/Desktop/task/2016-12-31_0300_US_FOX-News_Hannity.v4.vrt', 'r') as vrt_file:
    vrt_contents = vrt_file.read()

# Split the VRT contents into individual lines
lines = vrt_contents.split('\n')

# Create a new file called "segments.txt"
with open('segments.txt', 'w') as segments_file:
    # Write each line from the VRT file to the segments file,
    # but format it as "turnX-text TAB start TAB end"
    for line in lines:
        line = line.strip()
        segments_file.write(f"{line.decode('utf-8')} TAB {line.start} TAB {line.end}\n")

# Read the segments file and print each segment
with open('segments.txt', 'r') as segments_file:
    for line in segments_file:
        line = line.strip()
        print(line)