from marshmallow import Schema, fields

class PostSchema(Schema):
    user_id = fields.Int(required=True)
    content = fields.Str(required=True)

post_schema = PostSchema()
