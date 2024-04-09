# coding=utf-8
import sys
import json
import time
from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import urlencode

API_KEY = 'xxxx'
SECRET_KEY = 'xxxx'

CUID = '123456PYTHON'
RATE = 16000  # 固定值
DEV_PID = 1537  # 1537 表示识别普通话，使用输入法模型
ASR_URL = 'http://vop.baidu.com/server_api'
SCOPE = 'audio_voice_assistant_get'
TOKEN_URL = 'http://aip.baidubce.com/oauth/2.0/token'

class DemoError(Exception):
    pass

def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params).encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read().decode()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read().decode()
    result = json.loads(result_str)
    if 'access_token' in result and 'scope' in result:
        if SCOPE and (SCOPE not in result['scope'].split(' ')):
            raise DemoError('scope is not correct')
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

def audio_to_text(audio_path, output_path):
    token = fetch_token()
    with open(audio_path, 'rb') as speech_file:
        speech_data = speech_file.read()

    length = len(speech_data)
    if length == 0:
        raise DemoError('file %s length read 0 bytes' % audio_path)

    FORMAT = audio_path[-3:]
    params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID}
    params_query = urlencode(params)

    headers = {
        'Content-Type': 'audio/' + FORMAT + '; rate=' + str(RATE),
        'Content-Length': str(length)
    }

    req = Request(ASR_URL + "?" + params_query, speech_data, headers)
    try:
        begin = time.perf_counter()
        f = urlopen(req)
        result_str = f.read().decode()
        print("Request time cost %f" % (time.perf_counter() - begin))
    except URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read().decode()

    print(result_str)
    result = json.loads(result_str)
    if 'result' not in result:
        raise DemoError('no result found in asr response')

    with open(output_path, 'w') as output_file:
        output_file.write(result['result'][0])

