from flask import Flask

app = Flask("kdm-manager")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
