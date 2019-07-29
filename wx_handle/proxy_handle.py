# coding=utf-8
import time


class ProxyHandle(object):
    def __init__(self, msg):
        self.msg = msg

    def __create_instance(self):
        module_name = "wx_handle." + self.msg.MsgType + "_handle"
        class_name = self.msg.MsgType[0].upper() + self.msg.MsgType[1:].lower() + "Handle"
        module = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module, class_name)
        obj = class_meta(self.msg)
        return obj

    def deal(self):
        try:
            handle_proxy = self.__create_instance()
            return handle_proxy.deal()

        except Exception as e:
            print(e)
            param = dict()
            param['ToUserName'] = self.msg.FromUserName
            param['FromUserName'] = self.msg.ToUserName
            param['CreateTime'] = int(time.time())
            param['Content'] = "【未有处理该消息的方法】"
            text_data = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
            return text_data.format(**param)
