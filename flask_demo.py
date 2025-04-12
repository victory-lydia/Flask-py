# from flask import Flask

# app = Flask(__name__)

# @app.route('/hello')
# def index():
#     return "hello world"

# def username(name):
#     return f"username: {name}"

# app.add_url_rule("/hello/<name>", view_func=username)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask
app = Flask(__name__)

def index():
  return '<h1>Hello World!</h1>'
app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == "__main__":
    app.run(debug=True)