"""
@author: hao.ling
@Date: 2020/12/20 3:38 下午
@Annotation: 系统配置
"""

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey

from myPlatform.config.service import db


class System(db.Model):
    """系统信息表"""
    __tableName__ = "system"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="系统id")
    system_name = Column(String(64), unique=True, nullable=False, comment="系统名称")
    system_path = Column(String(64), nullable=True, comment="系统路径")
    status = Column(Boolean, server_default="0", comment="当前账户状态(0:启用,1:禁用)")
    create_id = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="创建者id")
    modify_id = Column(Integer, ForeignKey("user.user_id"), nullable=True, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
