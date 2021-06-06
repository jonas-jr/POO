from flask.helpers import flash
from werkzeug.utils import redirect, secure_filename
from app import app
from flask import request, render_template, jsonify, make_response
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signin")
def signin():
    return render_template('formCli.html')

@app.route("/inicio")
def inicio():
    return render_template('inicio.html')

@app.route("/inicioprof")
def inicioprof():
    return render_template('inicioprof.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return 'Upload feito com sucesso'

@app.route("/autentica", methods=["GET", "POST"])
def autentica():
    if request.method == "POST":
        user = request.form['usuario']
        pswrd = request.form['senha']
        erro=0
        if not len(user) >= 8:
            flash(message="O usuário deve ter no mínimo 8 caracteres")
            eroo=1
        if not len(pswrd) >= 8:
            flash(message="A senha deve ter 8 ou mais caracteres")
            erro=1
        if erro ==1:
            return redirect(request.url)
        return render_template('cliente.html', user=user, pswrd=pswrd)

    elif request.method == "GET":
        arguments = request.args
        if 'usuario' in arguments and 'senha' in arguments:
            usr = arguments.get('usuario')
            pswrd = arguments.get('senha')
            return render_template('cliente.html', user=usr, pswrd=pswrd)

    return '/login'

@app.route("/cadastrarCli", methods=["POST"])
def cadastrarCli():
    if request.is_json:
        req = request.get_json() 
        resposta = {
            'nome': req.get('nome'),
            'cpf': req.get('cpf'),
            'email': req.get('email'),
            'usr': req.get('usuario'),
            'pswrd': req.get('senha') 
        }
        resp = make_response(jsonify(resposta), 200)  #200 codiog indica que deu certo a requisição
        return resp
    else:
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        user = request.form['usuario']
        pswrd = request.form['senha']
        return render_template('cliente.html', nome=nome, cpf=cpf, email=email, user=user, pswrd=pswrd)

    return render_template('/signin')

