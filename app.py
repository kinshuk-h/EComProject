# import os
# import time

import flask
import dotenv
# from flask_httpauth   import HTTPTokenAuth
# from flask_session    import Session
from flask_sqlalchemy import SQLAlchemy

# from src import api, routes, utils
from src import utils

# Load the environment variables specific to the app.
dotenv.load_dotenv()

app = flask.Flask(__name__)

app.config.update(
    SECRET_KEY                     = os.environ.get('SECRET_KEY', 'so_secret_much_wow'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SQLALCHEMY_DATABASE_URI        = os.environ.get('DB_URL'),
    SESSION_TYPE                   = 'filesystem',
    SESSION_USE_SIGNER             = True
)

db       = SQLAlchemy(app)
# auth     = HTTPTokenAuth(scheme='Bearer')
# # Initialize a filesystem based server-side session
# Session(app)

engine   = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], { 'echo': False })
database = utils.database.get_instance(engine)

# @app.template_filter()
# def field(date, fmtstr):
#     return utils.format_date(date, fmtstr)

# @app.before_request
# def prepare_user():
#     flask.g.user = None
#     session_token = flask.session.get('user_token', None)
#     if session_token and session_token in tokens:
#         flask.g.user = tokens.get(session_token, None)
#     elif session_token:
#         flask.session.pop('user_token')

# @auth.verify_token
# def verify_token(token):
#     for _token, data in tokens.items():
#         if int(time.time()) - data['timestamp'] > 24 * 3600:
#             del tokens[_token]
#     if token in tokens:
#         return tokens[token]

# @auth.get_user_roles
# def get_user_roles(user):
#     if 'role' not in user:
#         user['role'] = database.get_user_role(user['ID'])
#     return user['role']

# Register the standard endpoints.
# app.register_blueprint(
#     routes.create_blueprint(
#         auth, tokens, database,
#     )
# )
# Register the API endpoint.
# app.register_blueprint(
#     api.create_blueprint(
#         auth, tokens, database,
#     )
# )

@app.route("/playground", methods=["GET", "POST"])
def playground():
    return flask.jsonify({
        'method': flask.request.method,
        'headers': { **flask.request.headers },
        'args': { key: utils.get_field(flask.request, key, allow_null=True) or '' for key in flask.request.args },
        'form': { key: utils.get_field(flask.request, key, allow_null=True) or '' for key in flask.request.form },
        'session': { **flask.session }
    })

@app.route("/")
def index():
    return "Under Development"
    # user = auth.current_user() or flask.g.user
    # if user:
    #     return flask.redirect(flask.url_for("routes.users.current_user"))
    # else:
    #     return flask.render_template(
    #         "ui/home_new_user.html.jinja",
    #         current_user=user
    #     )