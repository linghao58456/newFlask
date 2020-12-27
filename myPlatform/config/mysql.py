"""
@author: hao.ling
@Date: 2020/11/21 4:37 下午
@Annotation: 数据库配置
"""


def mysql():
    """
    数据库配置信息
    :return: 数据字典
    """
    host = "localhost"
    username = "root"
    password = "12345678"
    dbName = "myPlatform"
    port = 3306
    dbType = "mysql"
    connect = "pymysql"
    return {"host": host, "username": username, "password": password, "db": dbName, "port": port, "db_type": dbType,
            "connect": connect}
