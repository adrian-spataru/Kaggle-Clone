import datetime
from passlib.apps import custom_app_context as pwd_context
from db import db


class Competition(db.Model):
    """This is class represents the competition database table."""

    __tablename__ = 'competition'

    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String, index=True, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    data = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    public_ids = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    ending_at = db.Column(db.DateTime, default=(datetime.datetime.now()+ datetime.timedelta(days=1)))
    submissions = db.relationship("Submission", backref="competition", lazy="dynamic")

    def __init__(self, name, shortname, description, data, solution, public_ids, ending_at=None):
        self.name = name
        self.shortname = shortname 
        self.description = description
        self.data = data
        self.solution = solution
        self.public_ids = public_ids 
        if ending_at:
            self.ending_at = ending_at

