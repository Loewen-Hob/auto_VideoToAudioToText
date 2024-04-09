import ffmpeg
import subprocess
def audio_extract(input_path, output_path):
    command = [
        'ffmpeg', 
        '-i', input_path,
        '-acodec', 'pcm_s16le',
        '-ar', '16000',
        '-ac', '1',
        '-f', 'wav',
        output_path
    ]

    subprocess.run(command, check=True)
