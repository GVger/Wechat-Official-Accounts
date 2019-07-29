# coding = utf-8
from aip import AipNlp
from ai.baidu_ai.language.baidu_language_const import DepRelConstant
import configparser


class LanguageAi(object):
    def __init__(self, config_path):
        config = configparser.ConfigParser()
        config.read(config_path)
        self.__app_id = config["language"]["app_id"]
        self.__api_key = config["language"]["api_key"]
        self.__secret_key = config["language"]["secret_key"]
        self.__client = AipNlp(self.__app_id, self.__api_key, self.__secret_key)

    def __sentence_parse(self, sentence):
        json_str = self.__client.depParser(sentence)
        items = json_str["items"]
        parse = LanguageDeal(items)
        parse.deal()
        return json_str

    def reply_content(self, content):
        return self.__sentence_parse(content)


class LanguageDeal(object):
    def __init__(self, dict_sentence_parse):
        self.__items = dict_sentence_parse
        self.__sentence_core = dict()
        self.__sentence_head_list = dict()
        for item in self.__items:
            if item["deprel"] == DepRelConstant.HED:
                self.__sentence_core[item["id"]] = item
            head_list = self.__sentence_head_list.get(item["head"])
            if head_list is None:
                temp = list()
                temp.append(item)
                self.__sentence_head_list[item["head"]] = temp
            else:
                head_list.append(item)
        print("====================================")
        print(self.__sentence_core)
        print(self.__sentence_head_list)

    def deal(self):
        for key in self.__sentence_head_list:
            word_list = self.__sentence_head_list.get(key)
            for item in word_list:
                deprel = item["deprel"]
                if deprel == DepRelConstant.VOB:
                    print("动宾短语的宾语：" + item["word"])


if __name__ == "__main__":
    ai = LanguageAi("../baidu_ai.conf")
    ai.reply_content("今天不打羽毛球了？")
