# coding=utf-8

import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xmlData)
    elif msg_type == 'image':
        return ImageMsg(xmlData)
    elif msg_type == 'event':
        return EventMsg(xmlData)
    elif msg_type == 'voice':
        return VoiceMsg(xmlData)
    elif msg_type == 'video':
        return VideoMsg(xmlData)
    elif msg_type == 'shortvideo':
        return ShortVideoMsg(xmlData)
    elif msg_type == 'location':
        return LocationMsg(xmlData)
    elif msg_type == 'link':
        return LinkMsg(xmlData)


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text

        if self.MsgType != 'event':
            self.MsgId = xmlData.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text


class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text


class EventMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Event = xmlData.find('Event').text
        self.EventKey = xmlData.find('EventKey').text

        if self.Event == 'scancode_push' or self.Event == 'scancode_waitmsg':
            scan_code_info = xmlData.find('ScanCodeInfo')
            self.ScanType = scan_code_info.find('ScanType').text
            self.ScanResult = scan_code_info.find('ScanResult').text

        elif self.Event == 'pic_sysphoto'or self.Event == 'pic_photo_or_album'or self.Event == 'pic_weixin':
            send_pics_info = xmlData.find('SendPicsInfo')
            self.Count = send_pics_info.find('Count').text
            self.PicList = send_pics_info.find('PicList')

        elif self.Event == 'location_select':
            send_location_info = xmlData.find('SendLocationInfo')
            self.Location_X = send_location_info.find('Location_X').text
            self.Location_Y = send_location_info.find('Location_Y').text
            self.Scale = send_location_info.find('Scale').text
            self.Label = send_location_info.find('Label').text
            self.Poiname = send_location_info.find('Poiname').text


class VoiceMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text
        self.Format = xmlData.find('Format').text


class VideoMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text
        self.ThumbMediaId = xmlData.find('ThumbMediaId').text


class ShortVideoMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text
        self.ThumbMediaId = xmlData.find('ThumbMediaId').text


class LocationMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Location_X = xmlData.find('Location_X').text
        self.Location_Y = xmlData.find('Location_Y').text
        self.Scale = xmlData.find('Scale').text
        self.Label = xmlData.find('Label').text


class LinkMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Title = xmlData.find('Title').text
        self.Description = xmlData.find('Description').text
        self.Url = xmlData.find('Url').text
