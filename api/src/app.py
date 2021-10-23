from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

import send_data

cignal_remote = send_data.Cignal_remote()

app = Flask(__name__)
api = Api(app)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
#db = SQLAlchemy(app)

class Commands(Resource):
    def get(self, command):
        cignal_remote.send_command(command)

        return {'Command_sent' : command}

class Channel(Resource):
    def get(self, command):
        cignal_remote.send_channel_command(command)

        return {'Command_sent' : command}

api.add_resource(Commands, "/commands/<command>")
api.add_resource(Channel, "/channel/<command>")


@app.route('/')
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)