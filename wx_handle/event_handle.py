# coding=utf-8
from wx_handle.constant.event_constant import EventConstant


class EventHandle(object):
    def __init__(self, msg):
        self.msg = msg

    def deal(self):
        print("Event:",self.msg.Event)
        print("EventKey:", self.msg.EventKey)
        if self.msg.Event == EventConstant.CLICK:  # "CLICK":
            print("你点击了按钮", self.msg.EventKey, "对应的按钮")
        elif self.msg.Event == EventConstant.VIEW:  # "VIEW":
            print("跳转", self.msg.EventKey)
        elif self.msg.Event == EventConstant.SCAN_CODE_PUSH:  # "scancode_push":
            print("触发扫描推事件")
            print("扫描到的内容是：", self.msg.ScanResult)
        elif self.msg.Event == EventConstant.SCAN_CODE_WAIT_MSG:  # "scancode_waitmsg":
            print("触发扫描推带提示事件")
            print("扫描到的内容是：", self.msg.ScanResult)
        elif self.msg.Event == EventConstant.PIC_SYS_PHOTO:  # "pic_sysphoto":
            print("触发发送图片事件")
            print("发送图片数量：", self.msg.Count)
        elif self.msg.Event == EventConstant.PIC_PHOTO_OR_ALBUM:  # "pic_photo_or_album":
            print("触发发送拍照或相册图片事件")
            print("发送图片数量：", self.msg.Count)
        elif self.msg.Event == EventConstant.PIC_WEI_XIN:  # "pic_weixin":
            print("触发发送相册事件")
            print("发送图片数量：", self.msg.Count)
        elif self.msg.Event == EventConstant.LOCATION_SELECT:  # "location_select":
            print("触发发送定位事件")
            print("X：", self.msg.Location_X, "Y：", self.msg.Location_Y)
            print("Scale：", self.msg.Scale)
            print("地方名：", self.msg.Label)
            print("PoiName：", self.msg.Poiname)
        elif self.msg.Event == EventConstant.SUBSCRIBE:  # "subscribe":
            print(self.msg.FromUserName, "关注了")
        elif self.msg.Event == EventConstant.UNSUBSCRIBE:  # "unsubscribe":
            print(self.msg.FromUserName, "取关了")
        return "success"
