from teste import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/base')
def hello_world():
    return 'Hello Goku!'
