"""
@author: hao.ling
@Date: 2020/12/20 3:46 下午
@Annotation: 数据库配置
"""

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey

from myPlatform.config.service import db


class Database(db.Model):
    """数据库信息表"""
    __tableName__ = "database"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="数据库id")
    database_name = Column(String(64), unique=True, nullable=False, comment="数据库连接名称")
    database_host = Column(String(64), nullable=False, comment="数据库地址")
    database_username = Column(String(64), nullable=False, comment="数据库账号")
    database_password = Column(String(64), nullable=False, comment="数据库密码")
    base_name = Column(String(64), nullable=False, comment="数据库库名")
    status = Column(Boolean, server_default="0", comment="当前账户状态(0:启用,1:禁用)")
    create_id = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="创建者id")
    modify_id = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
