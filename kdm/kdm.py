import flask
from kdm.gear import controllers

app = flask.Flask("kdm")
app.register_blueprint(controllers.gear)

@app.route('/')
def landingPage():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
