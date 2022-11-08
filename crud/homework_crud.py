import uuid
from dbmodels import User, HomeworkRecord, HomeworkPicture, AverageGrade, FailedWork
from query2dict import queryToDict

from sqlalchemy import or_

import psycopg2
conn = psycopg2.connect(database="db_hwork", user="user_hwork",password="user_hwork@1234", host="117.78.1.34", port="26000")
cursor = conn.cursor()


class HomeworkCRUD:
    def __init__(self, db):
        self.db = db

    async def stu_upload_homework(self, name, stuid, teaid, stu_text, address=None):
        homework_id = str(uuid.uuid4())
        picture_id = str(uuid.uuid4())
        homework = HomeworkRecord(id=homework_id, name=name, stuid=stuid, teaid=teaid, stu_text=stu_text)
        picture = HomeworkPicture(picid=picture_id, workid=homework_id, address=address)
        self.db.add(homework)
        self.db.add(picture)
        self.db.commit()
        return True

    async def stu_get_homework(self, stu_id: str):
        homework = self.db.query(
            HomeworkRecord.id,
            HomeworkRecord.name,
            HomeworkRecord.score,
            HomeworkRecord.stuid,
            HomeworkRecord.teaid,
            HomeworkRecord.checked
        ).filter(
            or_(
                HomeworkRecord.stuid == stu_id,
                HomeworkRecord.teaid == stu_id
            )
        ).all()
        return queryToDict(homework)

    async def stu_get_homework_detail(self, homework_id: str):
        homework_detail = self.db.query(
            HomeworkRecord.id,
            HomeworkRecord.name,
            HomeworkRecord.score,
            HomeworkRecord.stuid,
            HomeworkRecord.teaid,
            HomeworkRecord.stu_text,
            HomeworkRecord.tea_text,
            HomeworkRecord.checked,
            HomeworkPicture.address
        ).join(
            HomeworkPicture,
            HomeworkPicture.workid == HomeworkRecord.id
        ).filter(
            HomeworkRecord.id == homework_id
        ).first()
        return queryToDict(homework_detail)

    async def stu_get_homework_checked(self, stu_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.stuid == stu_id,
            HomeworkRecord.checked == 1
        ).all()
        return queryToDict(homework)

    async def stu_get_homework_not_checked(self, stu_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.stuid == stu_id,
            HomeworkRecord.checked == 0
        ).all()
        return queryToDict(homework)

    async def stu_get_averagegrade(self, stu_id: str):
        average_grade = self.db.query(AverageGrade).filter(
            AverageGrade.sid == stu_id
        ).first()
        if average_grade is not None:
            return {'grade': average_grade.grade}
        else:
            return {'grade': 'null'}

    async def tea_get_homework(self, tea_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.stuid == tea_id
        ).all()
        return queryToDict(homework)

    async def tea_get_homework_checked(self, tea_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.tea_id == tea_id,
            HomeworkRecord.checked == 1
        ).all()
        return queryToDict(homework)

    async def tea_get_homework_not_checked(self, tea_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.tea_id == tea_id,
            HomeworkRecord.checked == 0
        ).all()
        return queryToDict(homework)

    async def tea_check_homework(self, homework_id, score, tea_text):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.id == homework_id
        ).first()
        stu_id = homework.stuid

        homework.score = score
        homework.tea_text = tea_text
        homework.checked = 1
        self.db.commit()

        cursor.execute("call hwork.gradeProc({})".format(stu_id))
        conn.commit()
        return []


    async def tea_get_failed_work(self):
        fail_works = self.db.query(
            HomeworkRecord.id,
            HomeworkRecord.name,
            HomeworkRecord.score,
            HomeworkRecord.stuid,
            HomeworkRecord.teaid,
            HomeworkRecord.stu_text,
            HomeworkRecord.tea_text
        ).filter(
            HomeworkRecord.score < 60
        ).all()
        return queryToDict(fail_works)

    async def tea_get_picture(self, workid: str):
        homework_picture = self.db.query(HomeworkPicture).filter(
            HomeworkPicture.workid == workid
        ).all()

        return queryToDict(homework_picture)
