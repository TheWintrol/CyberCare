from tokenize import Name
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Integer, nullable=False)
    url = date = db.Column(db.String(1000), nullable=False)
    comment = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Post(name= {name}, date={date}, url={url}, comment={comment})"


post_put_args = reqparse.RequestParser()

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'date': fields.Integer,
    'url': fields.String,
    'comment': fields.String
}


class Post(Resource):
    @marshal_with(resource_fields)
    def get(self, post_id):
        result = PostModel.query.filter_by(id=post_id).first()
        return result

    def put(self, post_id):
        args = post_put_args.parse_args()
        post - PostModel(id=post_id, name=args['name'], date=args['date']
                         url=args['url'], comment=args['comment'])
        db.session.add(post)
        return post


api.add_resource(Post, "/post/<int:post_id>")

if __name__ == "__main__":
    app.run(debug=True)
