# coding=utf-8

import util as wx_util


class Menu(object):
    def __init__(self, token):
        self.token = token
        self.create_menu_url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % token
        self.query_menu_url = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % token
        self.cleanup_menu_url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % token

    def create_menu(self):
        json_data = """
        {
            "button": [
                {
                    "type": "click", 
                    "name": "按钮", 
                    "key": "CLICK"
                },
                {
                    "name": "菜单",
                    "sub_button":[
                        {    
                           "type":"view",
                           "name":"跳转",
                           "url":"http://www.baidu.com/",
                           "key":"VIEW"
                        },
                        {
                            "type": "scancode_push", 
                            "name": "扫码推事件", 
                            "key": "scancode_push"
                        },
                        {
                            "type": "scancode_waitmsg", 
                            "name": "扫码带提示", 
                            "key": "scancode_waitmsg"
                        },
                        {
                            "type": "pic_sysphoto", 
                            "name": "系统拍照发图", 
                            "key": "pic_sysphoto"
                         }
                    ]
                },
                {
                    "name": "菜单2",
                    "sub_button": [
                        {
                            "type": "pic_photo_or_album",
                            "name": "系统拍照相册",
                            "key" : "pic_photo_or_album"
                        },
                        {
                            "type": "pic_weixin",
                            "name": "发送相册",
                            "key": "pic_weixin"
                        },
                        {
                            "type": "location_select",
                            "name": "发送定位",
                            "key": "location_select"
                        },
                        {
                            "type": "view_miniprogram",
                            "name": "跳转小程序",
                            "key": "view_miniprogram"
                        }
                    ]
                }
            ]
        }
        """
        return wx_util.do_post(self.create_menu_url, json_data.encode("utf-8"))

    def query_menu(self):
        return wx_util.do_get(self.query_menu_url)

    def cleanup_menu(self):
        return wx_util.do_get(self.cleanup_menu_url)


if __name__ == "__main__":
    menu = Menu("19_bD2SQEgsKmBZiAdLB52PSBiJa6Du9krVA0HshJVp0GiGJXO-NJsub-vohZdK7qHmlGnebh_ltW8hsgZ8IEMpuhi-d0Ao3ceiTOUGWAeS3vr-g8c_nAzO0aMqiUtI4CSrrpwV7rCwo_F9l4AEHDVbAHATPH")
    # json_result = str(menu.create_menu().read(), "utf-8")
    # print(json_result)
    menu_result = str(menu.query_menu().read(), "utf-8")
    print(menu_result)
