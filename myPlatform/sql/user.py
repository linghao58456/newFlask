"""
@author: hao.ling
@Date: 2020/11/21 9:44 下午
@Annotation: 用户表sql操作
"""

from myPlatform.public.connect import Connect


class User(Connect):
    def set_user_id(self, number: int):
        """
        设置用户id开始值
        :param number: 开始的数字
        :return: 成功，失败
        """
        try:
            self.cursor.execute(f"alter table user AUTO_INCREMENT={number}")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def insert_user_info(self, user_name: str, password: str):
        """
        新增用户信息
        :param user_name: 用户名
        :param password: 密码
        :return: 成功，失败
        """
        try:
            self.cursor.execute(f"insert into user (user_name,password) values ('{user_name}','{password}')")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def update_user_info(self, user_name: str, password=None, status=0):
        """
        更新用户信息
        :param user_name: 用户名
        :param password: 密码
        :param status: 状态，0：启用，1：禁用
        :return: 成功，失败
        """
        try:
            if password is not None:
                sql = f"update user set password='{password}' where user_name='{user_name}'"
            elif status == 1:
                sql = f"update user set status={status} where user_name='{user_name}'"
            else:
                sql = f"select * from user where user_name='{user_name}' and status={status}"
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def select_user_info(self, username=None, status=0):
        """
        查询用户信息
        :param username: 用户名
        :param status: 状态，0：启用，1：禁用
        :return:
        """
        if username is not None:
            sql = f"select * from user where user_name='{username}' and status={status}"
        else:
            sql = f"select * from user"
        self.cursor.execute(sql)
        user_list = self.cursor.fetchall()
        return user_list

    def select_user_password(self, username: str):
        """
        查询用户密码
        :param username: 用户名
        :return:
        """
        self.cursor.execute(f"select password from user where user_name='{username}'")
        password = self.cursor.fetchall()
        return password
