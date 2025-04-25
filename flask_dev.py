from flask import Flask
app = Flask(__name__)

def index():
  return '<h1>SIU WELCOMES YOU!</h1>'
app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def user(name):
 return '<h1>Welcome, {}!</h1>'.format(name)

if __name__ == "__main__":
    app.run(debug=True)
    
    with open('file.txt', 'r') as file:
      content = file.read()
      print(content)





#       from flask import Flask
# app = Flask(__name__)

# def index():
#   return '<h1>SIU WELCOMES YOU!</h1>'
# app.add_url_rule('/', 'index', index)

# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Welcome, {}!</h1>'.format(name)

# if __name__ == "__main__":
#     app.run(debug=True)
    