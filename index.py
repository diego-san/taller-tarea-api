from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
@app.route('/<token>')
def home(token=None):
    if token is None:
        return render_template("home.html", name=token)
    else:
        return token
        pass
    pass



if __name__ == '__main__':
    app.run(debug=True)
    pass