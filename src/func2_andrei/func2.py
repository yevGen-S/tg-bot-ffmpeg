import ffmpeg


def slow(stream):
    return stream.filter('asetrate', 37000)

def reverb(stream):
    impulse_response = ffmpeg.input(rf'C:\Users\andre\source\repos\Semestr 5\asm\audio\impulse_response\{reverb_name}')
    stream = ffmpeg.filter([stream, impulse_response], 'afir', dry=2, wet=2)
    return stream

# def reverb_complex(stream):
#     impulse_response = ffmpeg.input(r'C:\Users\andre\source\repos\Semestr 5\asm\audio\IR.wav')
#     reverb = ffmpeg.filter([stream, impulse_response], 'afir', dry=10, wet=10)
#     stream = ffmpeg.filter([stream, reverb], 'amix', inputs=2, weights=[2, 1])
#     return stream


in_name = 'big_tv_slowed.mp3'
out_name = 'big_tv_slowed_reverb.mp3'
reverb_name = 'IR.wav'


input = rf'C:\Users\andre\source\repos\Semestr 5\asm\audio\source\{in_name}'
output = rf'C:\Users\andre\source\repos\Semestr 5\asm\audio\out\{out_name}'

stream = ffmpeg.input(input)

stream = reverb(stream)

stream.output(output).run()
