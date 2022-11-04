import flask

from .. import utils

def create_blueprint(auth, tokens, database, *args, **kwargs):
    """ Creates a blueprint for exposing routes related the users section of the API
    Args:
        auth (flask_httpauth.HTTPTokenAuth): The flask http authentication object for restricting access
        tokens (dict): The currently maintained set of tokens for logged in users.
        database (sqlalchemy.engine.Engine): The engine object associated with the currently connected database.
        org_codes (utils.CodeGenerator): Generator for organization codes.
    Returns:
        flask.Blueprint: The blueprint object to register in the flask application.
    """

    blueprint = flask.Blueprint(
        'users', __name__,
        template_folder='templates',
        url_prefix='/users'
    )

    @blueprint.route('/view')
    @auth.login_required
    def view_user():
        user = auth.current_user()
        result = database.get_user_by_id(user['ID'])
        del result['password_Hash']
        del result['password_Salt']
        return flask.jsonify(result)

    @blueprint.route('/login', methods=[ 'POST' ])
    def login_user():
        username = utils.get_field(flask.request, 'username')
        password = utils.get_field(flask.request, 'password')

        result = database.get_user_by_ref(username)
        if not result:
            flask.abort(401, description="Failed to login user")
        if not utils.verify_password(password, result.Password_Hash):
            flask.abort(401, description="Failed to login user")

        token, data = utils.make_token(result.Username, result.ID)
        tokens[token] = data

        return flask.jsonify({
            'status': True,
            'code': 200,
            'username': result.Username,
            'token': token
        }), 200

    @blueprint.route('/create', methods=[ 'POST' ])
    def create_user():
        password  = utils.get_field(flask.request, 'password')
        hashed_pw, salt = utils.hash_password(password)

        params = {
            'user_id'      : None,
            'name'         : utils.get_field(flask.request, 'name'),
            'username'     : utils.get_field(flask.request, 'username'),
            'password_hash': hashed_pw,
            'password_salt': salt,
            'contact'      : utils.get_field(flask.request, 'contact'     , allow_null=True) or 0,
            'email'        : utils.get_field(flask.request, 'e-mail'      , allow_null=True),
        }

        database.execute((database.user.insert(), params))

        result = database.get_user_by_id(params['ID'])
        del result['password_hash']
        del result['password_salt']
        return flask.jsonify({
            'status': True,
            'code': 200,
            'data': result
        }), 200

    return blueprint