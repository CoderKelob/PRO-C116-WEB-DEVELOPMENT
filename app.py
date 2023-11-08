# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    return CreateMember("Bob", 14, "index.html")

# define the route to father webpage
@app.route("/father")
def father():
    return CreateMember("Father",43,"father.html")

# define the route to mother webpage
@app.route("/mother")
def mother():
    return CreateMember("Jane",42,"mother.html")

# define the route to friends webpage
@app.route("/friend")
def friends():
    return CreateMember("Javen",14,"friend.html")

def CreateMember(name,age,targetLocation):
    Name = name
    Age = age

    return render_template(targetLocation , name = Name , age = Age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
