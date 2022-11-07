import json

from flask import Flask, request, jsonify, Blueprint

from ext import db
from crud.user_crud import UserCRUD

us = Blueprint("user", __name__)  #蓝图的对象的名称=Blueprint('自定义蓝图名称',__name__)

user_crud = UserCRUD(db.session)

@us.route("/api/login", methods=['POST'])
async def login():
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))
    userid = json_data.get('userId')
    password = json_data.get('password')

    login_info = await user_crud.login_verify(userid, password)

    return jsonify(login_info)


@us.route("/api/user/register", methods=['POST'])
async def register():
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))
    name = json_data.get('name')
    gender = json_data.get('gender')
    password = json_data.get('password')
    return await user_crud.create_user(name, gender, password)


@us.route("/api/get/teacher/list")
async def get_tea():
    return await jsonify(user_crud.get_tea())

@us.route("/")
async def name_test():
    return await user_crud.name()
