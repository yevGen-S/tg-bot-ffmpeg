from __future__ import unicode_literals
import youtube_dl

"""
    Hook for logging moment when video is loaded.
"""


def finish_loading_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


"""
    This class is for loading audio and video from youtube by handling url link
"""


class YoutubeLoader:
    def gen_ydl_opts(self, type, user_id):
        if type == 'audio':
            ydl_opts = {
                'format': 'bestaudio',
                'outtmpl': '../input_' + type + 's/' + user_id + '.mp3',
                'noplaylist': True,
                'progress_hooks': [finish_loading_hook],
            }
            return ydl_opts

        if type == 'video':
            ydl_opts = {
                'format': 'worstvideo',
                'outtmpl': '../input_' + type + 's/' + user_id + '.mp4',
                'noplaylist': True,
                'progress_hooks': [finish_loading_hook],
            }
            return ydl_opts

    def loadVideo(self, url, user_id):
        with youtube_dl.YoutubeDL(self.gen_ydl_opts('video', user_id)) as ydl:
            ydl.extract_info(url)

    def loadAudio(self, url, user_id):
        with youtube_dl.YoutubeDL(self.gen_ydl_opts('audio', user_id)) as ydl:
            ydl.extract_info(url)


youtube_loader = YoutubeLoader()