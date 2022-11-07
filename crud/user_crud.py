import uuid

from dbmodels import User
from exception.not_found_exception import NotFoundException
from query2dict import queryToDict


class UserCRUD:
    def __init__(self, db):
        self.db = db

    async def create_user(self, name=None, gender=None, password=None):
        id = str(uuid.uuid4())
        user1 = User(userid=id, name=name, gender=gender, password=password)
        self.db.add(user1)
        self.db.commit()
        return id

    async def login_verify(self, id: str, password):
        """
        查询姓名
        :param id:
        :return:
        """
        user = self.db.query(User).filter(
            User.userid == id
        ).first()
        if not user:
            raise NotFoundException().with_message("this user is not found.")
        else:
            if user.password != password:
                status = False
            else:
                status = True
            if user.role == 0:
                isStudent = True
            else:
                isStudent =False
            return {'status': status, 'isStudent': isStudent}

    async def get_tea(self):
        return queryToDict(self.db.query(User.userid, User.name).filter(User.role == 1).all())


    async def name(self):
        return queryToDict(self.db.query(User.userid).filter(User.name == 'jzc').all())
