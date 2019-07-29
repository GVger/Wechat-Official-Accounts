# coding=utf-8
from configparser import ConfigParser
from aip import AipSpeech
from ai.baidu_ai.speech.baidu_ai_speech_const import BAIDU_AI_SPEECH_ERROR, BAIDU_AI_SPEECH_LANGUAGE


class Speech(object):
    def __init__(self, config_path):
        config = ConfigParser()
        config.read(config_path)
        self.__app_id = config["speech"]["app_id"]
        self.__api_key = config["speech"]["api_key"]
        self.__secret_key = config["speech"]["secret_key"]
        self.__client = AipSpeech(self.__app_id, self.__api_key, self.__secret_key)

    def parse(self, speech, format="pcm", rate=8000,
              dev_pid=BAIDU_AI_SPEECH_LANGUAGE.get("ONLY_CH_MANDARIN")):
        response = self.__client.asr(speech, format, rate, {
            "dev_pid": dev_pid
        })
        code = response.get("err_no")
        result = None
        if code == 0:
            result = response.get("result")
        else:
            print("百度语音解析失败，错误代码：{code}，原因：【{reason}】".format(code=code, reason=BAIDU_AI_SPEECH_ERROR.get(code)))
        return result

