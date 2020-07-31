# -*- coding: utf-8 -*-

import tushare as ts


class Downloader:
    def __init__(self):
        self.pro = ts.pro_api('66167463c58caad5dc528418ee1b52f3725a821588408c61b5915d92')


if __name__ == '__main__':
    d = Downloader()
    pass