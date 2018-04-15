import flask

app = flask.Flask("kdm")

@app.route('/')
def landingPage():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run()
