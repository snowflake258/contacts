from marshmallow import Schema, fields
from marshmallow.validate import Length


class ContactSchema(Schema):
    firstname = fields.Str(required=True, validate=Length(1, 30))
    lastname = fields.Str(required=True, validate=Length(1, 30))
    phone = fields.Str(required=True, validate=Length(1, 16))
    group_id = fields.Int(required=True)
