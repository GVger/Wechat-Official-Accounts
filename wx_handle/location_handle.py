# coding=utf-8
import wx.reply as reply


class LocationHandle(object):
    def __init__(self, msg):
        self.msg = msg
        self.to_user = msg.FromUserName
        self.from_user = msg.ToUserName

    def deal(self):
        label = self.msg.Label
        x = self.msg.Location_X
        y = self.msg.Location_Y
        content = "你当前的位置是：" + label + "，坐标为(" + x + "," + y + ")"
        text_reply = reply.TextReply(self.to_user, self.from_user, content)
        return text_reply.send()
