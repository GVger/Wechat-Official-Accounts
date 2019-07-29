# coding=utf-8
import wx.reply as reply


class LinkHandle(object):
    def __init__(self, msg):
        self.msg = msg
        self.to_user = msg.FromUserName
        self.from_user = msg.ToUserName

    def deal(self):
        title =  self.msg.Title
        description =  self.msg.Description
        url =  self.msg.Url
        content = "你发送的连接的标题：" + title + ",描述：" + description + "，url:" + url
        text_reply = reply.TextReply(self.to_user, self.from_user, content)
        return text_reply.send()
