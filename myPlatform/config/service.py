"""
@author: hao.ling
@Date: 2020/11/21 9:35 下午
@Annotation: 服务应用
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from myPlatform.config.mysql import mysql
from myPlatform.config.parameter import userId_number
from myPlatform.sql.user import User

db = SQLAlchemy()

mysql = mysql()
user = User()
number = userId_number()


def create_app():
    """
    创建项目实例
    :return: app实例
    """

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{mysql['db_type']}+{mysql['connect']}://{mysql['username']}:" \
                                            f"{mysql['password']}@{mysql['host']}:{mysql['port']}/{mysql['db']}"
    db.init_app(app)
    create_tables(app)
    user.set_user_id(number)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    注册蓝图
    :param app: 项目应用名称
    :return:
    """
    from myPlatform.api import api

    CORS(api, supports_credentials=True)
    app.register_blueprint(api, url_prefix='/api')


def create_tables(app):
    """
    创建数据库表结构模型
    :param app: 项目应用名称
    :return:
    """
    from myPlatform.model.user import User
    from myPlatform.model.database import Database
    from myPlatform.model.system import System

    db.create_all(app=app)
