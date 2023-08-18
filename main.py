import flask
from flask import *
from flask import render_template


app=Flask(__name__)

@app.route("/")
def saludar():
    return render_template("index.html")

@app.route("/hola/<nombre>")
def saludar_nombre(nombre):
    return "hola, %s" %nombre

@app.route("/bar/<int:edad>")
def validar_edad(edad):
    if edad >=18:
        return "bienvenido bro"
    else:
        return "a dormir bro"


@app.route("/num/<int:numero1>,<int:numero2>")
def validar_numero(numero1,numero2):
    return str(numero1+numero2)

@app.route("/admin")
def saludar_admin():
    return "q xopa jefe"



@app.route("/mortal/<nombre>")
def saluda_mortal(nombre):
    return "q xopa mortal %s" %nombre


@app.route("/login/<usuario>")
def sesion(usuario):
    if usuario == "admin":
        return redirect(url_for("saludar_admin"))
    else:
        return redirect(url_for("saluda_mortal",nombre=usuario))




if __name__ == "__main__":

    app.run(debug=True)

