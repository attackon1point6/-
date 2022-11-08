import json

from flask import Flask, request, jsonify

import configs
from ext import db
from views import user, homework
# from crud.use_crud import UserCRUD
from crud.homework_crud import HomeworkCRUD

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)

with app.app_context():
    connection = db.engine.raw_connection()
    cursor = connection.cursor()

app.register_blueprint(user.us)
app.register_blueprint(homework.hwork)

# @app.route('/user', methods = ['GET', 'POST'])
# async def add_user():
#     # engine = db.get_engine()
#     # conn = engine.connect()
#     """
#     // 增
#     user1 = User(name='zs', age=20)
#     db.session.add(user1)
#     db.session.commit()
#
#     // 查
#     user1 = User.query.filter(User.userid == userid).first()
#     """
#     # user1 = User(userid=2)
#     # db.session.add(user1)
#     # db.session.commit()
#     #user1 = User.query.filter(User.userid == 1).first()
#     # conn.close()  # 跟open函数一样，可以用with语句
#     return await user_crud.get_username(1)


@app.route('/api/check/homework', methods=['POST'])
async def tea_id_check_work():
    data = request.get_data()
    json_data = json.loads(data.decode('utf-8'))[0]
    homework_id = json_data.get('id')
    score = json_data.get('score')
    tea_text = json_data.get('tea_text')
    return await homework.homework_crud.tea_check_homework(cursor, homework_id, score, tea_text)


if __name__ == '__main__':
    app.run()
