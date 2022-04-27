from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("Inicio.html")

@app.route('/login', methods=["POST"])
def login():
    name = request.form.get("nombres")
    surename = request.form.get("apellidos")
    user = request.form.get("usuario")
    email = request.form.get("correo")
    password = request.form.get("contrasena")
    b_date = request.form.get("fecha")
    return render_template("Formulario_registro.html",
                            name=name, 
                            surename=surename,
                            user=user,
                            email=email,
                            password=password,
                            b_date=b_date)

if __name__=='__main__':
	app.run(debug=True, port=5000)