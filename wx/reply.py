# coding=utf-8
import time


class Reply(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextReply(Reply):
    def __init__(self, to_user_name, from_user_name, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return xml_form.format(**self.__dict)


class ImageReply(Reply):
    def __init__(self, to_user_name, from_user_name, media_id):
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = media_id

    def send(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return xml_form.format(**self.__dict)


class VoiceReply(Reply):
    def __init__(self, to_user_name, from_user_name, media_id):
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = media_id

    def send(self):
        xml_form = """
            <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[voice]]></MsgType>
            <Voice>
            <MediaId><![CDATA[{MediaId}]]></MediaId>
            </Voice>
            </xml>
        """
        return xml_form.format(**self.__dict)


class VideoReply(Reply):
    def __init__(self, to_user_name, from_user_name, media_id, title, description):
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = media_id
        self.__dict['Title'] = title
        self.__dict['Description'] = description

    def send(self):
        xml_form = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[video]]></MsgType>
                <Video>
                    <MediaId><![CDATA[{MediaId}]]></MediaId>
                    <Title><![CDATA[{Title}]]></Title>
                    <Description><![CDATA[{Description}]]></Description>
                </Video>
            </xml>
        """
        return xml_form.format(**self.__dict)


class MusicReply(Reply):
    def __init__(self,  to_user_name, from_user_name, title, description, music_url, hq_music_url, thumb_media_id):
        self.__dict = dict()
        self.__dict['ToUserName'] = to_user_name
        self.__dict['FromUserName'] = from_user_name
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Title'] = title
        self.__dict['Description'] = description
        self.__dict['MusicURL'] = music_url
        self.__dict['HQMusicUrl'] = hq_music_url
        self.__dict['ThumbMediaId'] = thumb_media_id

    def send(self):
        xml_form = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[music]]></MsgType>
            <Music>
                <Title><![CDATA[{Title}]]></Title>
                <Description><![CDATA[{Description}]]></Description>
                <MusicUrl><![CDATA[{MusicURL}]]></MusicUrl>
                <HQMusicUrl><![CDATA[{HQMusicUrl}]]></HQMusicUrl>
                <ThumbMediaId><![CDATA[{ThumbMediaId}]]></ThumbMediaId>
            </Music>
        </xml>
         """
        return xml_form.format(**self.__dict)

