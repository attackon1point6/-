import json

from flask import Flask, request, jsonify, Blueprint

from ext import db
from crud.homework_crud import HoHomeworkCRUD

hwork = Blueprint("homework", __name__)  #蓝图的对象的名称=Blueprint('自定义蓝图名称',__name__)

homework_crud = HoHomeworkCRUD(db.session)


@hwork.route('/homework/stu/upload', methods=['POST'])
async def stu_upload_homework():
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))
    name = json_data.get('name')
    stuid = json_data.get('stu_id')
    teaid = json_data.get('teaid')
    stu_text = json_data.get('stu_text')
    address = json_data.get('address')
    return await homework_crud.stu_upload_homework(name, stuid, teaid, stu_text, address)


@hwork.route('/homework/stu/<stu_id>')
async def stu_get_work(stu_id: str):
    # data = request.get_data()
    # json_data = json.loads(data.decode('utf-8'))
    # stu_id = json_data.get('stu_id')
    return await jsonify(homework_crud.stu_get_homework(stu_id))


@hwork.route('/homework/stu/<stu_id>/checked')
async def stu_get_checked_work(stu_id: str):
    # data = request.get_data()
    # json_data = json.loads(data.decode('utf-8'))
    # stu_id = json_data.get('stu_id')
    checked_work = await homework_crud.stu_get_homework_checked(stu_id)
    return jsonify(checked_work)


@hwork.route('/homework/stu/<stu_id>/not_checked')
async def stu_get_not_checked_work(stu_id: str):
    # data = request.get_data()
    # json_data = json.loads(data.decode('utf-8'))
    # stu_id = json_data.get('stu_id')
    not_checked_work = await homework_crud.stu_get_homework_not_checked(stu_id)
    return jsonify(not_checked_work)


@hwork.route('/homework/stu/<hwork_id>/detail')
async def stu_get_homework_detail(hwork_id: str):
    return await homework_crud.stu_get_homework_detail(hwork_id)


@hwork.route('/homework/stu/<stu_id>/grade')
async def stu_get_averageGrade(stu_id: str):
    return await homework_crud.stu_get_averagegrade(stu_id)


@hwork.route('/homework/tea/<tea_id>')
async def tea_get_homework(tea_id: str):
    return await homework_crud.tea_get_homework(tea_id)

@hwork.route('/homework/tea/<tea_id>/checked')
async def tea_id_get_checked_work(tea_id: str):
    # data = request.get_data()
    # json_data = json.loads(data.decode('utf-8'))
    # stu_id = json_data.get('stu_id')
    checked_work = await homework_crud.tea_get_homework_checked(tea_id)
    return jsonify(checked_work)


@hwork.route('/homework/tea/<tea_id>/not_checked')
async def tea_id_get_not_checked_work(tea_id: str):
    # data = request.get_data()
    # json_data = json.loads(data.decode('utf-8'))
    # stu_id = json_data.get('stu_id')
    not_checked_work = await homework_crud.stu_get_homework_not_checked(tea_id)
    return jsonify(not_checked_work)


@hwork.route('/homework/tea/<homework_id>/check', methods=['POST'])
async def tea_id_check_work(homework_id: str):
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))
    score = json_data.get('score')
    tea_text = json_data.get('tea_text')
    return await homework_crud.tea_check_homework(homework_id, score, tea_text)


@hwork.route('/homework/tea/<tea_id>/failedstu')
async def tea_get_failed_stu(tea_id: str):
    failed_stu = await homework_crud.tea_get_failed_stu(tea_id)
    return jsonify(failed_stu)


@hwork.route('/homework/tea/<workid>/picture')
async def tea_get_picture(workid: str):
    picture = await homework_crud.tea_get_picture(workid)
    return jsonify(picture)
