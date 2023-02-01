import ffmpeg
import os


""" 
 -stream_loop -1 : to loop infinity of video input stream
 -map 0:v:0 : pick the video of the first input stream
 -map 1:a:0 : pick the audio of the second input stream
 -shortest : select the shortest length of input streams, which is the audio stream since the video will be looped infinity
 -c copy : no video and audio transcodes.
"""


def merge_audio_and_looped_video(video_name, audio_name, output_name):
    command = f'ffmpeg -stream_loop -1 -i ../input_videos/{video_name}.mp4 -i ../input_audios/{audio_name}.mp3  -map ' \
              f'0:v:0 -map 1:a:0 -shortest ../processed/{output_name}.mp4 '
    os.system(command)
