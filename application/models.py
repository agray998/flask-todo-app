from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    desc = db.Column(db.String(100), default='Add a description')
    status = db.Column(db.String(10), default='Incomplete')

