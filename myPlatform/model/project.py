"""
@author: hao.ling
@Date: 2021/1/9 11:07 上午
@Annotation: 项目表
"""

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey

from myPlatform.config.service import db


class Project(db.Model):
    __tableName__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="项目id")
    project_name = Column(String(64), unique=True, nullable=False, comment="项目名称")
    project_address = Column(String(64), nullable=True, comment="项目地址")
    project_manager = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="项目负责人")
    status = Column(Boolean, server_default="0", comment="当前账户状态(0:启用,1:禁用)")
    create_id = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="创建者id")
    modify_id = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
