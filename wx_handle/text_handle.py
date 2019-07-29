# coding=utf-8
import wx.reply as reply
from wx_handle.text_reply.text import TextDeal


class TextHandle(object):
    def __init__(self, msg):
        self.msg = msg
        self.to_user = msg.FromUserName
        self.from_user = msg.ToUserName

    def deal(self):
        rec_text_content = self.msg.Content
        content = rec_text_content
        text_deal = TextDeal(content)
        text_reply = reply.TextReply(self.to_user, self.from_user, text_deal.get_reply_content())
        return text_reply.send()
