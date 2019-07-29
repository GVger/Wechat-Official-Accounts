# coding=utf-8
from aip import AipImageClassify
import configparser


class ImageAi(object):
    def __init__(self, conf_path):
        config = configparser.ConfigParser()
        config.read(conf_path)
        self.__app_id = config["image"]["app_id"]
        self.__api_key = config["image"]["api_key"]
        self.__secret_key = config["image"]["secret_key"]
        self.__client = AipImageClassify(self.__app_id, self.__api_key, self.__secret_key)

    def deal(self, image):
        return self.__client.advancedGeneral(image)
