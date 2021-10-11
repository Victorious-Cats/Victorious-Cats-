from flask import Flask, render_template, request, session ,url_for,redirect
import random

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

@app.route("/emote_radio", methods=["POST"])
def emote_radio():
    # list of random response, feel free to modify it so it look nicer
    sad =["Oh No! Lets do something fun today to cheer you up","Don't worry my friend, you alway have me by your side"]
    happy =["Yay, great to see you feeling good, you make me feel good also","Amazing, it's time for you to spread this positive energy to others"]
    neutral=["Ok, fair enough","Your day could be even better after you talk with me"]
    option = int(request.form['emote_radio_output'])
    
    message = ""
    if option < 3:
        message += random.choice(sad)
    elif option >3:
        message += random.choice(happy)
    else:
        message += random.choice(neutral)
    text = f"{message}"
    return render_template("emote_response.html", text=text)

@app.route("/long_response", methods=["POST"])
def long_response():
    #list of positive key words, add more here pls since my vocabulary is limited
    positive=["good","great","excellent","amazing","happy","perfect","well", "cool", "fun", "neat", "nice", "positive", "joyous", "exciting", "wonderful", "refreshing", "invigorating", "wowza", "enjoyable"]
    #Same here for negative key words
    negative=["bad","terrible","ugly","horrible","sad","dissapointed","down", "depressed", "miserable", "moody", "worn out", "tired", "exhausted", "poor", "sick"]
    #Random response for each of them, feel free to add more
    positive_response=["Oh my god, that's a very cool story from you, I'm so happy to hear that","Yayyy, that's so good, you are such an amazing person, hope you could keep this emotion forerver", "Hell Yeah!", "That's so cool that you had a good day!", "It's days like these that you will remember when you're older!", "Wow! Thats Awesome!"]
    negative_response=["Oops, not a good thing to hear, I suggest you should go watch Squid Game, surely it can make your day better","I'm so sorry to hear that, but I think when you shared it with me, at least you have released your negative energy for the rest of the day", "Oh no!, You arent feeling well? That's rough buddy", "That sucks but lets try and look on the bright side! It's a beautiful day to be here", "Nooo! Let's try and make your day a bit better, how about some fresh air?", "Thats no good! Maybe some sunshine on a nice walk will help you feel better?"]
    
    response = request.form["textbox"]
    reply=""
    if any(word in response for word in positive):
        reply += random.choice(positive_response)
    elif any(word in response for word in negative):
        reply += random.choice(negative_response)
    else:
        #this is in case no given key words has been found, I dont know what to say so Ima leave it like this, feel free to edit
        reply += "Interesting!"
    text = f"{reply}"
    return render_template("long_response.html", text=text)
#register user to be complete after I figure out the database
# def register()
#also same for comparing user radio input from the past
# def comparing_input() 
if __name__=="__main__":
    app.run(debug=True)
