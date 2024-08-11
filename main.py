#Importações
from flask import Flask, render_template, url_for

#Inicio
app = Flask(__name__)


#Rota Princinpal
@app.route("/main")
def get_main():
    return render_template('index.html')


#Rota dos Produtos
@app.route("/produtos")
def get_produtos():
    return render_template('produtos.html')


#Rota do Cadastro
@app.route("/cadastrar")
def get_login():
    return render_template('login.html')





#Modo editor = On / Final
app.run(debug=True)