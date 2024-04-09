from translate import Translator
import re
import threading

def should_not_translate(text):
    """检查文本是否不需要翻译."""
    if text in ("", '\n') or re.match(r"^[0-9]+$", text) or \
        re.match(r"\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}", text):
        return True
    return False

def add_newline_if_missing(s):
    """确保字符串以换行符结尾."""
    return s if s.endswith('\n') else s + '\n'

def translate_text(translator, text):
    """翻译文本，并根据需要添加换行符."""
    if should_not_translate(text):
        return add_newline_if_missing(text.rstrip('\n'))
    return add_newline_if_missing(translator.translate(text.rstrip('\n')))

def translate_lines(segment, translator):
    """翻译文本行的列表."""
    return [translate_text(translator, line) for line in segment]

def thread_worker(lines, start, end, translator, result_map, index):
    """线程工作函数."""
    segment = lines[start:end]
    result_map[index] = translate_lines(segment, translator)
    print(f"Thread {index} processed lines {start} to {end}")

def parallel_translate(lines, translator, thread_count):
    """并行翻译文本行."""
    result_map = {}
    threads = []
    n = len(lines)
    segment_length = n // thread_count

    for i in range(thread_count):
        start = i * segment_length
        end = (i + 1) * segment_length if i != thread_count - 1 else n
        thread = threading.Thread(target=thread_worker, args=(lines, start, end, translator, result_map, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # 合并结果
    result = []
    for i in range(thread_count):
        result.extend(result_map[i])
    return result

def do_translate(source_file, target_file, source_lang, target_lang, thread_count):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    with open(source_file, 'r', encoding='utf-8') as f1, open(target_file, 'w', encoding='utf-8') as f2:
        lines = f1.readlines()
        translated_lines = parallel_translate(lines, translator, thread_count)
        f2.writelines(translated_lines)

if __name__ == '__main__':
    do_translate('test.srt', 'test1.srt', 'zh', 'en', 4)
