# coding=utf-8
from common.constant_base import ConstantBaseBase


class EventConstant(object):
    __constant = ConstantBaseBase()

    __constant.CLICK = "CLICK"
    __constant.VIEW = "VIEW"
    __constant.SCAN_CODE_PUSH = "scancode_push"
    __constant.SCAN_CODE_WAIT_MSG = "scancode_waitmsg"
    __constant.PIC_SYS_PHOTO = "pic_sysphoto"
    __constant.PIC_PHOTO_OR_ALBUM = "pic_photo_or_album"
    __constant.PIC_WEI_XIN = "pic_weixin"
    __constant.LOCATION_SELECT = "location_select"
    __constant.SUBSCRIBE = "subscribe"
    __constant.UNSUBSCRIBE = "unsubscribe"

    # 暴露的常量
    vars = locals()
    for key in __constant.__dict__:
        vars[key] = __constant.__dict__[key]
