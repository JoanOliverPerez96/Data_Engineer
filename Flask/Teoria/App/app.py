from flask import Flask, render_template


# Flask es una instancia WSGI y por eso la clase la instanciamos en una 
# variable app

                     # Para crear dicha instancia, debemos pasar como 
                      # primer argumento el nombre del módulo o paquete 
                      # de la aplicación. Para estar seguros de ello, 
                      # utilizaremos la palabra reservada __name__. 
                      # Esto es necesario para que Flask sepa, por ejemplo, 
                      # donde encontrar las plantillas de nuestra aplicación 
                      # o los ficheros estáticos.
app = Flask(__name__, instance_relative_config=True)
# app.config.from_object("config")
# app.config.from_pyfile("config.py")

@app.route('/')         # @app es un decorador que nos ayuda a indicarle a python
                        # que route pertenece a flask.
def index():
    return "<h1>Hello Worldsss!</h1>"

app.add_url_rule("/","index",index)

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)

@app.route("/user1/<name>")
def user1(name):
    return "<h1>Bye, {}!</h1>".format(name)

@app.route("/about")
def learn():
    return "Flask for web developers!"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/indice")
def indice():
    return render_template(r"Flask\Teoria\App\templates\mobile-app-html-template\index.html")

@app.route("/user/<name>/<int:index>")
def index2(name, index):
    mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
    mydict = {'key': 'valor'}
    mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
    return render_template("test.html", name=name, myindex=index, mylist=mylist, mydict=mydict, mytuple=mytuple)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

# app.run(debug=True)
