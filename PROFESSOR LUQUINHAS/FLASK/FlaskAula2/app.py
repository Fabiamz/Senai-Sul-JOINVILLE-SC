from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/alunos")
def mostrar_alunos():
    alunos = [
        {"nome": "Paulo", "idade": 21, "nota": 8.5},
        {"nome": "Mariana", "idade": 22, "nota": 9.0},
        {"nome": "Pedro", "idade": 20, "nota": 7.5},
        {"nome": "Ana", "idade": 23, "nota": 8.0},
        {"nome": "Lucas", "idade": 21, "nota": 9.5},
        {"nome": "Beatriz", "idade": 22, "nota": 8.8},
        {"nome": "Rafael", "idade": 20, "nota": 7.0},
        {"nome": "Camila", "idade": 23, "nota": 9.2},
    ]
    return render_template("alunos.html", lista_alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)