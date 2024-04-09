import ffmpeg
import subprocess

# def audio_extract(input, output):
# 	ffmpeg.input(input, vn=None).output(output).run()

# 解决中文路径ffmpeg无法运行的问题
# def audio_extract(input_path, output_path):
# 	command = [
# 		'ffmpeg', 
# 		'-i', 'pipe:0',  # 从stdin读取输入
# 		'-vn',          # 仅提取音频
# 		output_path     # 输出文件路径
# 	]

# 	with open(input_path, 'rb') as f:
# 		subprocess.run(command, input=f.read())

def audio_extract(input_path, output_path):
    command = [
        'ffmpeg', 
        '-i', input_path,  # 直接指定输入文件路径
        '-vn',             # 仅提取音频
        '-acodec', 'libmp3lame',  # 指定音频编码器为MP3
        output_path        # 输出文件路径
    ]

    subprocess.run(command, check=True)
