"""
@author: hao.ling
@Date: 2021/1/9 11:08 上午
@Annotation: 用户信息表
"""

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func

from myPlatform.config.service import db


class User(db.Model):
    __tableName__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True, comment="用户id")
    user_name = Column(String(64), unique=True, nullable=False, comment="用户名")
    real_name = Column(String(64), nullable=True, comment="用户姓名")
    password = Column(String(64), nullable=False, comment="密码")
    status = Column(Boolean, server_default="0", comment="当前账户状态(0:启用,1:禁用)")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
