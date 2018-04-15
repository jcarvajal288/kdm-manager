from flask import Flask

app = Flask("kdm-manager")

@app.route('/')
def hello_world():
    return 'Hello, World!'
