import pyaudio 
import requests
import base64
import wave
import time
import sys
import os
from FetchToken import fetch_token
TOP_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(TOP_DIR, "audio/my.wav")


def get_audio(file):
    """
    获取音频文件
    """
    with open(file, 'rb') as f:
        data = f.read()
    return data

def speech2text(speech_data, token, dev_pid):
    """
    音频转文字
    """
    FORMAT = 'wav'
    RATE = '16000'
    CHANNEL = 1
    CUID = 'baidu_workshop'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')
    data = {
        'format': FORMAT,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': token,
        'dev_pid': dev_pid
    }


    # 语音转文字接口 该接口可能每个人不一样，取决于你需要哪种语音识别功能，本文使用的是 语音识别极速版

    url = 'https://vop.baidu.com/pro_api'
    headers = {'Content-Type': 'application/json'} # 请求头
    print('正在识别...')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    print(Result)
    if 'result' in Result:
        return Result['result'][0]
    else:
        return Result


if __name__ == "__main__":
    TOKEN = fetch_token() # 获取token
    speech = get_audio(FILEPATH)
    speech2text(speech,TOKEN,int(80001))