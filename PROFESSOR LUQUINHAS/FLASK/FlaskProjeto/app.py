from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def listar_produtos():
    produtos = [
        {"nome": "Cacho de banana", "preco": 10.99, "estoque": 3},
        {"nome": "Maçã", "preco": 5.49, "estoque": 2},
        {"nome": "Laranja", "preco": 7.29, "estoque": 20},
        {"nome": "Pera", "preco": 6.99, "estoque": 15}
    ]
    return render_template("produtos.html", listar_produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)