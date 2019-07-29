# coding=utf-8
from wx_handle.text_reply.ai_text import AiText


class TextDeal(object):
    def __init__(self, content):
        self.__content = content
        self.__ai_text = AiText()

    def get_reply_content(self):
        return self.__ai_text.get_reply(self.__content)
