import ffmpeg

"""
    Class for editing audio. Takes path to audio, applies filters and output new edited audio file.
"""

# IR_church = 'IR.wav'
# IR_hall_1 = 's1r2_0_1.mp3'
# IR_hall_2 = 'ir_row_1l_sl_centre.wav'
# IR_church = 'church.mp3'
# IR_mausoleum = 'mausoleum.wav'
IR_studio = 'studio_1.wav'


class AudioEditor:
    def __init__(self, file_name):
        self.path = rf'.\input_audios\{file_name}'
        self.stream = ffmpeg.input(self.path)

    def change_speed(self, coefficient):
        self.stream = self.stream.filter('asetrate', int(self.get_audio_frequency() * coefficient))
        return self

    def reverb(self, wet=2):
        impulse_response = ffmpeg.input(rf'.\impulse_responses\{IR_studio}')
        self.stream = ffmpeg.filter([self.stream, impulse_response], 'afir', dry=10-wet, wet=wet)
        return self

    def bass_boost(self, gain=15, frequency=100):
        self.stream = self.stream.filter('bass', gain=gain, frequency=frequency)
        return self

    def change_pitch(self, pitch_scale):
        self.stream = self.stream.filter('rubberband', pitch=pitch_scale)
        return self

    # should async?
    def save(self, output_file_name, audio_format='mp3'):
        self.stream.output(rf'.\processed\{output_file_name}.{audio_format}').global_args('-y').run()

    # private methods
    def get_audio_frequency(self):
        return int(ffmpeg.probe(self.path)['streams'][0].get('sample_rate'))


# start_time = time.time()
# AudioEditor('1342722628.mp3').reverb().save('jma_slowed_pitched')
# print(time.time() - start_time)
# print(glob.glob(r".\input_audios\443426428.*")[0][glob.glob(r".\input_audios\443426428.*")[0].rindex('\\') + 1:])
