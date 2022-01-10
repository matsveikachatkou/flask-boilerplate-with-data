from flask import Flask

app = Flask(__name__)

# Routes go here
@app.route('/')
def run():
  return "I am running!"

@app.route('/<name>')
def say_hello(name):
  return "Hello " + str(name)

if __name__ == "__main__":
  app.run(debug=True)