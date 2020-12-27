"""
@author: hao.ling
@Date: 2020/11/21 9:39 下午
@Annotation: md5加密
"""

import hashlib

from myPlatform.config.parameter import parameter


def makeMd5(password: str):
    """
    md5加密
    :param password: 密码:string
    :return: 大写加密字符串:string
    """
    key = parameter()
    value = key + password
    result = hashlib.md5(value.encode("utf-8")).hexdigest()
    return result.upper()
