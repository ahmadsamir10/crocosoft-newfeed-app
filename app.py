from flask import Flask
from flask_restful import Api
from resources.post_resource import PostResource, PostListResource  # Importing resources

app = Flask(__name__)
api = Api(app)

# Define routes for the resources
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')

if __name__ == '__main__':
    app.run(debug=True)
