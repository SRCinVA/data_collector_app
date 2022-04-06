from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")  # for our index page
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        print(email)
        return render_template("success.html")

if __name__ == "__main__": #meaning that this is script is being executed and NOT imported
    app.debug=True
    app.run()  #we'll run the application in the default port (5000)
