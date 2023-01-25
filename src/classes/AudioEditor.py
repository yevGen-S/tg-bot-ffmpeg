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
    def __init__(self, path):
        self.stream = ffmpeg.input(path)
        self.path = path

    def slow_down(self, coefficient):
        self.change_speed(-coefficient)
        return self

    def speed_up(self, coefficient):
        self.change_speed(coefficient)
        return self

    def change_speed(self, coefficient):
        self.stream = self.stream.filter('asetrate', int(self.get_audio_frequency() * (1 + coefficient)))

    def reverb(self, dry=2, wet=2):
        impulse_response = ffmpeg.input(rf'../impulse_responses/{IR_studio}')
        self.stream = ffmpeg.filter([self.stream, impulse_response], 'afir', dry=dry, wet=wet)
        return self

    #async
    def save(self, path):
        self.stream.output(path).global_args('-y').run()

    def get_audio_frequency(self):
        return int(ffmpeg.probe(self.path)['streams'][0].get('sample_rate'))

    def bassboost(self, gain=15, frequency=100 ):
        self.stream = self.stream.filter('bass', gain=gain, frequency=frequency)
        return self


# in_name = 'jma.mp3'
# out_name = 'jma_slowed_bassboosted.mp3'
#
# input = rf'C:\Users\andre\source\repos\Semestr 5\asm\audio\source\{in_name}'
# output = rf'C:\Users\andre\source\repos\Semestr 5\asm\audio\out\{out_name}'
#
# audio = AudioEditor(input).slow_down(0.15).bassboost().save(output)