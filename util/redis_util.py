# coding=utf-8
import redis
import configparser


class Redis(object):
    def __init__(self, redis_config):
        config = configparser.ConfigParser()
        config.read(redis_config)
        redis_host = config["redis"]["host"]
        redis_port = config["redis"]["port"]
        redis_pw = config["redis"]["password"]
        self.__pool = redis.ConnectionPool(host=redis_host, port=redis_port, password=redis_pw, decode_responses=True)
        self.__connection = redis.StrictRedis(connection_pool=self.__pool)
        self.__error_flag = False

    def set_data(self, key, value, expire=7000):
        self.__error_flag = False
        try:
            self.__connection.set(key, value)
            self.__connection.expire(key, expire)
        except Exception as e:
            print("redis设置数据失败，原因：【{reason}】".format(reason=e))
            self.__error_flag = True

    def get_data(self, key):
        self.__error_flag = False
        try:
            data = self.__connection.get(key)
            return data
        except Exception as e:
            print("redis获取数据失败，原因：【{reason}】".format(reason=e))
            self.__error_flag = True

    def is_error(self):
        return self.__error_flag
