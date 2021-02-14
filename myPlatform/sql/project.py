"""
@author: hao.ling
@Date: 2021/1/9 11:10 上午
@Annotation: 项目表操作
"""

from myPlatform.public.connect import Connect


class Project(Connect):
    def select_project_info(self, current, size, project_name=None):
        """
        查询项目信息
        :param current:
        :param size: 数量
        :param project_name: 项目名称
        :return:
        """
        if project_name is not None:
            sql = f"select * from project where project_name='{project_name}'"
        else:
            sql = f"select * from project limit {current},{size}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def insert_project_info(self, project_name: str, project_address: str, project_manager: int, createId: int):
        """
        新增项目信息
        :param project_name: 项目名称
        :param project_address: 项目地址
        :param project_manager: 项目负责人
        :param createId: 创建者
        :return:
        """
        try:
            self.cursor.execute(
                f"insert into project (project_name,project_address,project_manager，create_id) values ('{project_name}"
                f"'{project_address}',{project_manager},{createId})")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def update_project_info(self, project_id: int, project_name: str, project_address: str, status: int):
        """
        更新项目信息
        :param project_id: 项目id
        :param project_name: 项目名称
        :param project_address: 项目地址
        :param status: 状态
        :return:
        """
        try:
            self.cursor.execute(
                f"update project set (project_name,project_address,status) values ('{project_name}','{project_address}'"
                f",{status}) where id='{project_id}'")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False
