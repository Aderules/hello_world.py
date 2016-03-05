from flask import Flask
from os import environ

app=Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"


@app.route("/hello/<name>")
def hello_person(name):
    html="""
        <h1>
           Hello  {}
        </h1>
        <p>
          Here's a picture of a kitten. Awwww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
  
@app.route("/jedi/<firstname>/<lastname>")
def name_jedi(firstname,lastname):
    html="""
        <h1>
           Your jedi name is {1:.3}{0:.2}
        </h1>
    """
    return html.format(firstname.lower(),lastname.lower())

    
if __name__=="__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))