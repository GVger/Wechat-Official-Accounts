# coding=utf-8
import wx.reply as reply
from io import BytesIO
import util.wx_util as wx_util
from ai.baidu_ai.image.image import ImageAi
from util.wx_util import WxUtil
from multiprocessing import Lock
import json


class ImageHandle(object):
    def __init__(self, msg):
        self.msg = msg
        self.to_user = msg.FromUserName
        self.from_user = msg.ToUserName
        self.__ai = ImageAi("../ai/baidu_ai/baidu_ai.conf")

    def deal(self):
        media_id = self.msg.MediaId
        image_url = self.msg.PicUrl
        image = BytesIO(wx_util.do_get(image_url).read())
        text = self.__ai.deal(image.getbuffer())
        image_reply = reply.ImageReply(self.to_user, self.from_user, media_id)
        wechat_util = WxUtil("../common/wx_system.conf")
        wechat_util.send_kf_msg(self.to_user, wechat_util.get_token(Lock()), json.dumps(text, ensure_ascii=False))
        return image_reply.send()
