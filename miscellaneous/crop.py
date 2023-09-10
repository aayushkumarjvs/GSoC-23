from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def crop_video(video_id, start_time, end_time):
    # Assuming the video_id is the path to the video
    video_path = f"{video_id}.mp4"
    cropped_video_path = f"{video_id}_cropped.mp4"

    # start_time and end_time should be in seconds
    ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=cropped_video_path)

    print(f"Cropped video is saved as {cropped_video_path}")
    return cropped_video_path
