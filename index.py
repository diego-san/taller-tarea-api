from flask import Flask, render_template
import requests
import json



app = Flask(__name__)

@app.route("/")
@app.route('/<token>')
def home(token=None):
    if token is None:
        return render_template("home.html")
    else:
        link = 'https://graph.facebook.com/v3.2/me?fields=id%2Cname%2Cage_range%2Cemail%2Cgender%2Cbirthday%2Clink%2Cpicture&access_token='+token
        dato = requests.get(link)
        dt = json.loads(dato.content.decode("utf-8"))


        """
        pasa dato de json a lista codigo viejo
        arreglo = []
        for obtener in dt:
            arreglo.append(dt[obtener])
            if obtener == 'picture':
                cantidad = len(arreglo)
                arreglo[cantidad - 1] = dt[obtener]['data']['url']
                pass
            pass
            """


        return render_template("datos.html", name = dt)
        pass
    pass



if __name__ == '__main__':
    app.run(debug=True)
    pass