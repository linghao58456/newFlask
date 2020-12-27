"""
@author: hao.ling
@Date: 2020/11/21 9:43 下午
@Annotation: 数据库连接
"""

import pymysql
from myPlatform.config.mysql import mysql


class Connect:
    def __init__(self):
        """初始化数据库连接"""
        database = mysql()
        self.db = pymysql.Connect(host=database['host'], user=database['username'], password=database['password'],
                                  port=database['port'], database=database['db'])
        self.cursor = self.db.cursor()
