"""
@author: hao.ling
@Date: 2021/1/9 1:37 下午
@Annotation: 用户接口
"""

from flask import jsonify, request

from myPlatform.api import api

from myPlatform.middleLayer.users import Users

user = Users()


# 注册
@api.route("/register", methods=["POST"])
def user_register():
    data = request.get_json()
    response = user.insert_user(data['username'], data['password'])
    return jsonify(response)


# 登录
@api.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    response = user.login_user(data['username'], data['password'])
    return jsonify(response)


# 查询用户
@api.route("/searchUser", methods=["GET"])
def user_search():
    data = request.args.get("username")
    response = user.select_user(data)
    return jsonify(response)


# 重置密码
@api.route("/resetPwd", methods=["POST"])
def user_reset():
    data = request.get_json()
    response = user.update_user(data['username'], data['password'])
    return jsonify(response)


# 修改密码
@api.route("/changePwd", methods=["POST"])
def user_change():
    data = request.get_json()
    response = user.update_user(data['username'], data['newPwd'], data['oldPwd'])
    return jsonify(response)
