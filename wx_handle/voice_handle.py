# coding=utf-8
import wx.reply as reply
from util.wx_util import WxUtil
from multiprocessing import Lock
from io import BytesIO
from ai.baidu_ai.speech.speech import Speech
import json


class VoiceHandle(object):
    def __init__(self, msg):
        self.msg = msg
        self.to_user = msg.FromUserName
        self.from_user = msg.ToUserName

    def deal(self):
        media_id = self.msg.MediaId
        voice_format = self.msg.Format
        wx_util = WxUtil("../common/wx_system.conf")
        voice = BytesIO(wx_util.get_media(wx_util.get_token(Lock()), media_id))
        speech_ai = Speech("../ai/baidu_ai/baidu_ai.conf")
        ai_result = speech_ai.parse(voice.getbuffer(), format=voice_format)
        if ai_result is None:
            voice_text = "未能识别该语音"
        else:
            voice_text = ai_result
        wx_util.send_kf_msg(self.to_user, wx_util.get_token(Lock()), json.dumps(voice_text, ensure_ascii=False))
        voice_reply = reply.VoiceReply(self.to_user, self.from_user, media_id)
        return voice_reply.send()
