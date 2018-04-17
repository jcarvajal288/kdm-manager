import flask

blueprint = flask.Blueprint('gear', __name__)

@blueprint.route('/gear', methods=['GET'])
def getAllGear():
    return 'all gear'
