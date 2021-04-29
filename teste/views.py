from teste import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/base')
def base():
    return 'Hello Goku!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
