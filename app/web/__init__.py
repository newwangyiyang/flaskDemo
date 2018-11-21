"""
    视图函数(controller)层的初始化
"""
from flask import Blueprint

web = Blueprint('web', __name__)

# 视图模块必须放在蓝图的下面（默认让视图模块执行，否则视图模块不生效）
from app.web import bookWeb
