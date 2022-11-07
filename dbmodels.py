from ext import db


class User(db.Model):
    __table_args__ = {"schema": 'hwork'}
    __tablename__ = "user_sys"
    userid = db.Column(db.VARCHAR, primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.Integer)
    password = db.Column(db.String(50))
    gender = db.Column(db.Integer)


class HomeworkRecord(db.Model):
    __table_args__ = {"schema": 'hwork'}
    __tablename__ = "homework"
    id = db.Column(db.VARCHAR, primary_key=True)
    name = db.Column(db.String(200))
    score = db.Column(db.Float)
    stuid = db.Column(db.Integer)
    teaid = db.Column(db.Integer)
    stu_text = db.Column(db.String(200))
    tea_text = db.Column(db.String(200))
    check = db.Column(db.Integer)


class HomeworkPicture(db.Model):
    __table_args__ = {"schema": 'hwork'}
    __tablename__ = "picture"
    picid = db.Column(db.VARCHAR, primary_key=True)
    workid = db.Column(db.VARCHAR)
    address = db.Column(db.String(200))


class FailedWork(db.Model):
    __table_args__ = {"schema": 'hwork'}
    __tablename__ = "failedwork"
    workid = db.Column(db.VARCHAR, primary_key=True)
    score = db.Column(db.Float)
    stuid = db.Column(db.VARCHAR)
    teaid = db.Column(db.VARCHAR)


class AverageGrade(db.Model):
    __table_args__ = {"schema": 'hwork'}
    __tablename__ = "averageGrade"
    sid = db.Column(db.VARCHAR, primary_key=True)
    grade = db.Column(db.Float)
