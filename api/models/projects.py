#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

# Title
# • Details
# • Total target (i.e 250000 EGP)
# • Set start/end time for the campaign (validate the date formula)


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    details = db.Column(db.String(1000))
    total_target = db.Column(db.Integer)
    user_id = db.Column(db.Float)

    def __init__(self, title, details,total_target,user_id):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.user_id = user_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ProjectSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Project
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    details = fields.String(required=True)
    total_target = fields.Float(required=True)
    user_id = fields.Integer(required=True)
