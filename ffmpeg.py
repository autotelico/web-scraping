import ffmpeg

stream = ffmpeg.input('space-complexity.mp4')
stream = stream.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)