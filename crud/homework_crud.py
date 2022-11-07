import uuid

from dbmodels import User, HomeworkRecord, HomeworkPicture, AverageGrade, FailedWork
from query2dict import queryToDict

class HoHomeworkCRUD:
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
        return homework_id

    async def stu_get_homework(self, stu_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.stuid == stu_id
        ).all()
        return list(map(
            self.__convert_homework, homework
        ))

    async def stu_get_homework_detail(self, homework_id: str):
        homework_detail = self.db.query(
            HomeworkRecord.id,
            HomeworkRecord.name,
            HomeworkRecord.score,
            HomeworkRecord.stuid,
            HomeworkRecord.teaid,
            HomeworkRecord.stu_text,
            HomeworkRecord.tea_text,
            HomeworkRecord.check,
            HomeworkRecord.address,
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
            HomeworkRecord.check == 1
        ).all()
        return list(map(
            self.__convert_homework, homework
        ))

    async def stu_get_homework_not_checked(self, stu_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.stuid == stu_id,
            HomeworkRecord.check == 0
        ).all()
        return list(map(
            self.__convert_homework, homework
        ))

    async def stu_get_averagegrade(self, stu_id: str):
        average_grade = self.db.query(AverageGrade).filter(
            AverageGrade.sid == stu_id
        ).first()
        return {'grade': average_grade.grade}

    async def tea_get_homework(self, tea_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.stuid == tea_id
        ).all()
        return list(map(
            self.__convert_homework, homework
        ))

    async def tea_get_homework_checked(self, tea_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.tea_id == tea_id,
            HomeworkRecord.check == 1
        ).all()
        return list(map(
            self.__convert_homework, homework
        ))

    async def tea_get_homework_not_checked(self, tea_id: str):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.tea_id == tea_id,
            HomeworkRecord.check == 0
        ).all()
        return list(map(
            self.__convert_homework, homework
        ))

    async def tea_check_homework(self, homework_id, score, tea_text):
        homework = self.db.query(HomeworkRecord).filter(
            HomeworkRecord.id == homework_id
        ).update({
            'score': score,
            'tea_text': tea_text,
            'check': 1
        })
        self.db.commit()
        return "checked"

    async def tea_get_failed_stu(self, tea_id):
        fail_stus = self.db.query(
            User.name,
            User.userid,
            FailedWork.workid,
            FailedWork.score
        ).join(
            FailedWork.stuid == User.userid
        ).filter(
            FailedWork.teaid == tea_id
        ).all()

        return queryToDict(fail_stus)

    async def tea_get_picture(self, workid: str):
        homework_picture = self.db.query(HomeworkPicture).filter(
            HomeworkPicture.workid == workid
        ).all()

        return queryToDict(homework_picture)

    @classmethod
    def __convert_homework(cls, homework: HomeworkRecord) -> dict:
        return {'id': homework.id,
                'name': homework.name,
                'score': homework.score,
                'teaid': homework.teaid,
                'check': homework.check}
