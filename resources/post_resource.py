from flask_restful import Resource
from flask import request
from marshmallow import ValidationError
from schemas.post_schema import post_schema  # Importing the schema for validation
from query_builders.post_query_builder import PostQueryBuilder
from db_connection import db_connection

class PostListResource(Resource):
    def post(self):
        try:
            # Validate request body
            data = post_schema.load(request.json)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        with db_connection() as conn:
            post_query = PostQueryBuilder(conn)
            post_id = post_query.create_post(data['user_id'], data['content'])

        return {"post_id": post_id, "message": "Post created successfully"}, 201


class PostResource(Resource):
    def get(self, post_id):
        with db_connection() as conn:
            post_query = PostQueryBuilder(conn)
            post = post_query.get_post(post_id)

        if post:
            post_data = {
                "id": post[0],
                "user_id": post[1],
                "content": post[2],
                "created_at": post[3].isoformat()
            }
            return post_data
        else:
            return {"message": "Post not found"}, 404

    def put(self, post_id):
        try:
            # Validate request body
            data = post_schema.load(request.json)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        with db_connection() as conn:
            post_query = PostQueryBuilder(conn)
            post_query.update_post(post_id, data['content'])

        return {"message": "Post updated successfully"}

    def delete(self, post_id):
        with db_connection() as conn:
            post_query = PostQueryBuilder(conn)
            post_query.delete_post(post_id)

        return {"message": "Post deleted successfully"}
