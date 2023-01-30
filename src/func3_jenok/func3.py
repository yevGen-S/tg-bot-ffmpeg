import ffmpeg


def load_video(name):
    input_video = ffmpeg.input(f'../input_videos/{name}')
    return input_video


def load_audio(name):
    input_audio = ffmpeg.input(f'../input_audios/{name}')
    return input_audio


def merge_video_and_audio(video_name, audio_name, output_name):
    try:
        command = (ffmpeg
                   .concat(load_video(video_name), load_audio(audio_name), v=1, a=1)
                   .output(f'../processed/{output_name}')
                   )
        command.run()
    except:
        err_msg = "Something go wrong! Video wasn't merged with audio"
        return err_msg
