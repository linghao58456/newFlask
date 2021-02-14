"""
@author: hao.ling
@Date: 2021/2/9 3:41 下午
@Annotation: 项目操作
"""
from myPlatform.sql.project import Project


class Projects:
    def __init__(self):
        self.project = Project()

    def select_project(self, current=0, size=10, project_name=None):
        """
        查询项目
        :param current: 页码
        :param size: 页数
        :param project_name: 项目名称
        :return:
        """
        result = self.project.select_project_info(current, size, project_name)
        project_list = []
        for res in result:
            project_list.append({"project_id": res[0], "project_name": res[1], "project_address": res[2],
                                 "project_manager": res[3], "status": res[4], "createId": res[5],
                                 "modifyId": res[6], "create_time": res[7], "modify_time": res[8]})
        return {"code": 1000, "data": project_list, "message": "success"}

    def insert_project(self, project_name, project_address, project_manager, createId):
        """
        新增项目
        :param project_name: 项目名称
        :param project_address: 项目地址
        :param project_manager: 项目负责人
        :param createId: 创建者id
        :return:
        """
        result = self.project.insert_project_info(project_name, project_address, project_manager, createId)
        if result:
            response = self.select_project(project_name=project_name)
            return response
        else:
            return {"code": 9999, "data": [], "message": "添加失败，请重试"}
