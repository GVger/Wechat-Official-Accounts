# coding=utf-8

import hashlib
import web
import wx.msg as msg
from wx_handle.proxy_handle import ProxyHandle
import configparser


class Handle(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("Wechat-Official-Accounts.conf")
        self.__token = config["wechat-official-accounts"]["token"]

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = self.__token

            # 进行加密操作，然后和公众号设置的进行对比
            list_hash = [token, timestamp, nonce]
            list_hash.sort()
            sha1 = hashlib.sha1()
            sha1.update(list_hash[0].encode("utf-8"))
            sha1.update(list_hash[1].encode("utf-8"))
            sha1.update(list_hash[2].encode("utf-8"))
            hashcode = sha1.hexdigest()  # 获取加密串

            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as e:
            return e

    def POST(self):
        try:
            web_data = web.data()
            print("=================================================")
            print("Handle Post webdata is:", web_data)
            print("=================================================")

            rec_msg = msg.parse_xml(web_data)
            # 收到消息之后的处理
            handle = ProxyHandle(rec_msg)
            return handle.deal()
        except Exception as e:
            return e

