"""
@author: hao.ling
@Date: 2020/11/21 9:37 下午
@Annotation: api蓝图
"""
from flask import Blueprint

api = Blueprint("api", __name__)

from myPlatform.api import errors
from myPlatform.api.views import user, project
