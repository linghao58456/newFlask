"""
@author: hao.ling
@Date: 2021/2/14 1:55 下午
@Annotation: 项目接口
"""
from flask import jsonify, request

from myPlatform.api import api
from myPlatform.middleLayer.projects import Projects

project = Projects()


# 查询项目
@api.route("/projectList", methods=["GET"])
def project_search():
    data = request.args.get("project_name")
    current = request.args.get("currentPage")
    size = request.args.get("pageSize")
    response = project.select_project(current=current, size=size, project_name=data)
    return jsonify(response)
