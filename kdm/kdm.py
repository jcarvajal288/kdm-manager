import flask
from kdm.gear import routes as gearRoutes

app = flask.Flask("kdm")
app.register_blueprint(gearRoutes.blueprint)

@app.route('/')
def landingPage():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
