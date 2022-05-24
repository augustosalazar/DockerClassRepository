from flask import Flask , redirect , url_for , request # Importing the class flask
# app is the object or instance of Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

# app.route informs Flask about the URL to be used by function
@app.route('/success/<name>')
# Creating a function named success
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['GET','POST'])
# Creating a function named login 
def login():
    if request.method == 'POST':
       user = request.form['adamlistek']
       return redirect(url_for('success', name = user)) 
    else:
       return "INVALID"
# Programs executes from here in a development server (locally on your system) 
# with debugging enabled. 
  
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=int("5000"), debug=True)