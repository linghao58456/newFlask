"""
@author: hao.ling
@Date: 2020/12/6 1:52 下午
@Annotation: 用户操作
"""
from myPlatform.sql.user import User
from myPlatform.public.markMd5 import makeMd5


class Users:
    def __init__(self):
        self.user = User()

    def select_user(self, username=None, status=0):
        """
        查询用户
        :param status: 状态
        :param username: 用户名
        :return:
        """
        result = self.user.select_user_info(username, status)
        if len(result) > 0:
            user_list = []
            for res in result:
                user_list.append(
                    {"userId": res[0], "username": res[1], "real_name": res[2], "status": res[4],
                     "createTime": res[5], "modifyTime": res[6]})
            return {"code": 1000, "data": user_list, "message": "success"}
        return {"code": 9999, "data": {}, "message": "用户名错误"}

    def insert_user(self, username, password):
        """
        新增用户
        :param username: 用户名
        :param password: 密码
        :return:
        """
        result = self.select_user(username)
        if result['code'] == 9999:
            newPwd = makeMd5(password)
            response = self.user.insert_user_info(username, newPwd)
            if response:
                new_result = self.select_user(username)
                return {"code": 1000, "data": new_result['data'], "message": "success"}
            return {"code": 9999, "data": {}, "message": "fail,请重试"}
        return {"code": 9999, "data": result['data'], "message": "用户已存在"}

    def login_user(self, username: str, password: str):
        """
        用户登录
        :param username: 用户名
        :param password: 密码
        :return:
        """
        result = self.select_user(username)
        if result['code'] == 1000:
            newPwd = makeMd5(password)
            sqlPwd = self.user.select_user_password(username)
            for pwd in sqlPwd:
                if pwd[0] == newPwd:
                    return {"code": 1000, "data": result['data'], "message": "success"}
                return {"code": 9999, "data": {}, "message": "账号密码错误"}
        return result

    def update_user(self, username: str, password: str, old_password=None):
        """
        更新用户
        :param old_password: 旧密码
        :param username: 用户名
        :param password: 密码
        :return:
        """
        result = self.select_user(username)
        if result['code'] == 1000:
            newPwd = makeMd5(password)
            if old_password is not None:
                oldPwd = makeMd5(old_password)
                resultPwd = self.user.select_user_password(username)
                for pwd in resultPwd:
                    if oldPwd == pwd[0]:
                        response = self.user.update_user_info(username, newPwd)
                        if response:
                            return {"code": 1000, "data": {}, "message": "success"}
                        return {"code": 9999, "data": {}, "message": "失败请重试"}
                    return {"code": 9999, "data": {}, "message": "旧密码不正确"}
            response = self.user.update_user_info(username, newPwd)
            if response:
                return {"code": 1000, "data": {}, "message": "success"}
            return {"code": 9999, "data": {}, "message": "失败请重试"}
        return result
