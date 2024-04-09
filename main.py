import os
import yaml
from tqdm import tqdm
from script import audio_tool, text_bd_tool, translate_tool

def process_video(input_video_path, output_audio_path, srt_path):

    audio_tool.audio_extract(input_video_path, output_audio_path)
    print("Audio extraction success.")

    text_bd_tool.audio_to_text(output_audio_path, srt_path)
    print("Text extraction success.")

    # 可以根据需要启用翻译部分
    # translate_tool.do_translate(srt_path, srt_translate_path, config['from'], config['to'], config['translate_threads'])
    # print("Translation success.")

    print(f"Processing {input_video_path} success.")

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    return False

if __name__ == '__main__':
    with open('config.yaml', encoding='utf-8') as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)

    video_folder_path = config['input_folder']
    mp3_folder_path = config['output_folder']
    srt_folder_path = config['srt_folder']

    # 遍历视频文件夹下的所有子文件夹
    for subdir in tqdm(os.listdir(video_folder_path), desc='Processing videos'):
        subdir_path = os.path.join(video_folder_path, subdir)
        if os.path.isdir(subdir_path):  # 确保是文件夹
            for filename in tqdm(os.listdir(subdir_path), desc='Processing videos in'+ subdir):
                if filename.endswith(".mp4"):  # 检查文件扩展名
                    input_video_path = os.path.join(subdir_path, filename)
                    base_filename = os.path.splitext(filename)[0]

                    # 为每个视频文件的输出创建子目录
                    output_audio_dir = os.path.join(mp3_folder_path, subdir)
                    srt_output_dir = os.path.join(srt_folder_path, subdir)

                    output_audio_path = os.path.join(output_audio_dir, base_filename + '.wav')
                    srt_path = os.path.join(srt_output_dir, base_filename + '.srt')

                    if ensure_dir(output_audio_path) and ensure_dir(srt_path):
                        process_video(input_video_path, output_audio_path, srt_path)

                    else:
                        print(f"Skipping {input_video_path} because output directory exists.")
