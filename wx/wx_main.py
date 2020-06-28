# coding=utf-8

import os
import sys
import web
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from wx.handle import Handle

urls = (
    "/", "Handle"
)


if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))  # 当前项目路径加入
    app = web.application(urls, globals())
    app.run()
