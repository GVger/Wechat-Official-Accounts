# coding=utf-8
import urllib.request
import configparser
import json
from util.wx_const import WX_CONST
from util.redis_util import Redis
from multiprocessing import Lock


def do_get(url):
    resp = urllib.request.urlopen(url)
    return resp


def do_post(url, data):
    req = urllib.request.Request(url=url, data=data)
    resp = urllib.request.urlopen(req)
    return resp


class WxUtil(object):
    class NotInstance(TypeError):
        pass

    def __init__(self, wx_config):
        self.__config_path = wx_config
        self.__config = configparser.ConfigParser()
        self.__config.read(wx_config)

    def send_kf_msg(self, open_id, token, content):
        custom_url = self.__config["url"]["custom"].format(token=token)
        template = {
            "touser": open_id,
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        # ensure_ascii防止序列化的时候变成ascii
        data = json.dumps(template, ensure_ascii=False).encode("utf-8")
        info = do_post(url=custom_url, data=data).read()
        code = json.loads(info).get("errcode")
        if code != 0:
            print("发送客服消息失败，错误代码：【{code}】,原因：【{reason}】".format(code=code, reason=WX_CONST.get(code)))

    def get_token(self, lock):
        # if not isinstance(lock, Lock):
        #     raise self.NotInstance("need a Lock type")
        # else:
        lock.acquire()
        token = self.__get_token()
        lock.release()
        return token

    def __get_token(self):
        redis = Redis(self.__config_path)
        key = self.__config["keyword"]["token_redis_key"]
        token = redis.get_data(key)
        if redis.is_error():
            return None
        else:
            if token is None:
                app_id = self.__config["wx-system-info"]["app_id"]
                app_secret = self.__config["wx-system-info"]["app_secret"]
                token_url = self.__config["url"]["token"]
                url = token_url.format(appid=app_id, secret=app_secret)
                json_str = str(do_get(url).read(), "utf-8")
                print("============================================")
                print("token接口返回:{token}".format(token=json_str))
                print("============================================")
                json_obj = json.loads(json_str)
                errcode = json_obj.get("errcode")
                if errcode is not None:
                    print("获取token失败，原因：【{reason}】".format(reason=WX_CONST.get(errcode)))
                else:
                    access_token = json_obj.get("access_token")
                    expires_in = json_obj.get("expires_in")
                    redis.set_data(key, access_token, expires_in)
                    return access_token
            else:
                return token

    def get_media(self, token, media_id):
        media_url = self.__config["url"]["media"]
        url = media_url.format(token=token, media_id=media_id)
        response = do_get(url=url).read()
        return response
