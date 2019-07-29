# coding=utf-8
import util.wx_util as wx_util
import configparser


def get_media_url(token, media_id):
    config = configparser.ConfigParser()
    config.read("wx_system.conf")
    media_url = config["url"]["media"]
    url = media_url.format(token=token, media_id=media_id)
    return url


if __name__ == "__main__":
    main_url = get_media_url()
    print(str(wx_util.do_get(main_url).read(), "utf-8"))
