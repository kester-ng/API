from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields,marshal_with 
from flask_sqlalchemy import SQLAlchemy
from model.VideoModel import VideoModel
from main import db

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Name of the video", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': field.String,
    'views': fields.Integer,
    'likes': field.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)
        return result

    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201