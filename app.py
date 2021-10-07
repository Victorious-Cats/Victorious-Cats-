from flask import Flask, render_template, request, session ,url_for,redirect

app = Flask(__name__)
app.secret_key = "hello"
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method =="POST":
        user = request.form["username"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return render_template("emote_quote.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)
