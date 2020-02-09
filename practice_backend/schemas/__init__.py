from marshmallow import Schema, fields


class User(Schema):
    username = fields.Str()
    password = fields.Str()
