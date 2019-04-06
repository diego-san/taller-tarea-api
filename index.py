from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
@app.route('/<token>')
def home(token=None):
    if token is None:
        return render_template("home.html", name=token)
    else:
        link = 'https://graph.facebook.com/v3.2/me?fields=id,name,location,about,last_name,email,accounts,picture,gender,likes,session_key&access_token='+token

        return link
        pass
    pass



if __name__ == '__main__':
    app.run(debug=True)
    pass