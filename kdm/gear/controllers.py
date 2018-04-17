import flask

gear = flask.Blueprint('gear', __name__)

@gear.route('/gear', methods=['GET'])
def getAllGear():
    return 'all gear'
