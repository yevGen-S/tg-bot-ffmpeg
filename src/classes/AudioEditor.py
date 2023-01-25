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
        self.path = fr'../input_audios/{file_name}'
        self.stream = ffmpeg.input(self.path)

    def slow_down(self, coefficient):
        self.change_speed(-coefficient)
        return self

    def speed_up(self, coefficient):
        self.change_speed(coefficient)
        return self

    def reverb(self, dry=2, wet=2):
        impulse_response = ffmpeg.input(rf'../impulse_responses/{IR_studio}')
        self.stream = ffmpeg.filter([self.stream, impulse_response], 'afir', dry=dry, wet=wet)
        return self

    def bassboost(self, gain=15, frequency=100):
        self.stream = self.stream.filter('bass', gain=gain, frequency=frequency)
        return self

    def change_pitch(self, pitch_scale):
        self.stream = self.stream.filter('rubberband', pitch=pitch_scale)
        return self

    #should async?
    def save(self, output_file_name, audio_format='mp3'):
        self.stream.output(rf'../processed/{output_file_name}.{audio_format}').global_args('-y').run()

    #private methods
    def get_audio_frequency(self):
        return int(ffmpeg.probe(self.path)['streams'][0].get('sample_rate'))

    def change_speed(self, coefficient):
        self.stream = self.stream.filter('asetrate', int(self.get_audio_frequency() * (1 + coefficient)))



AudioEditor('jma.mp3').slow_down(0.2).change_pitch(0.8).save('jma_slowed_pitched')
