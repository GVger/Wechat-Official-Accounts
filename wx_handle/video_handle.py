# coding=utf-8
import wx.reply as reply


class VideoHandle(object):
    def __init__(self, msg):
        self.msg = msg
        self.to_user = msg.FromUserName
        self.from_user = msg.ToUserName

    def deal(self):
        media_id = self.msg.MediaId
        video_reply = reply.VideoReply(self.to_user, self.from_user, media_id, "测试标题", "测试描述")
        return video_reply.send()
