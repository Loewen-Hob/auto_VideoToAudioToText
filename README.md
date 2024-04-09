# auto_VideoToAudioToText

`auto_VideoToAudioToText` 是一个全自动的工具，旨在帮助用户将视频文件批量转换为音频文件，然后再将这些音频文件转换为文本字幕。此外，它还支持将生成的字幕翻译成其他语言，为用户提供一站式的视频内容处理解决方案。

## 功能特点

- **全自动处理**：自动将视频文件转换为音频文件，再将音频转换为文本字幕。
- **批量转换**：支持批量处理多个视频文件，大大提高工作效率。
- **多语言翻译**：支持将文本字幕翻译成多种语言。

## 安装说明

本项目依赖于 Python 3.6 或更高版本。你可以通过以下命令克隆并安装项目：

```bash
git clone https://github.com/Loewen-Hob/auto_VideoToAudioToText.git
cd auto_VideoToAudioToText
pip install -r requirements.txt
```

## 使用方法

1. 去百度智能云白嫖一下语音识别的免费额度，并在 ` text_bd_tool.py` 文件中配置好。

   eg：对百度的api想了解的更详细，可以在这学习：[speech-demo](https://github.com/Baidu-AIP/speech-demo)
	```
	API_KEY = '4oCl3SRxxx'
	SECRET_KEY = '2LFHfgRxxx'
	```


2. 在 ` config.yaml` 文件中配置这些基础设置。

	```
   input_folder: test/video
   output_folder: test/audio
   srt_folder: test/ASR
	```

3. run ` main.py` 即可。

## 配置选项

你可以通过编辑 `config.yaml` 文件来调整一些配置。

## 依赖关系

请查阅 `requirements.txt` 文件以获取项目依赖的详细列表。
