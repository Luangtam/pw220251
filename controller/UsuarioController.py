from app import app
from flask import render_template, request, jsonify
from sqlalchemy.orm import sessionmaker

from model.Conexao import engine
from model.Usuario import Usuario

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route('/usuarios', methods=['GET'])
def usuarios():
    db = SessionLocal()
    usuarios = db.query(Usuario).all()
    return jsonify([usuario.to_dict() for usuario in usuarios]),200

@app.route('/usuarios/novo', methods=['GET'])
def novo():
    return render_template("index.html")

@app.route('/usuarios/salvar', methods=['POST'])
def create():
    db = SessionLocal()
    usuario = Usuario(nome=request.form['nome'],
                      data=request.form['aniversario'])
    db.add(usuario)
    db.commit()
    return jsonify({'msg': 'salvo com sucesso'}), 200

@app.route("/usuarios/<int:id>", methods=['GET'])
def get_usuarios(id):
    db = SessionLocal()
    usu = db.query(Usuario).get(id)
    if (usu):
        return jsonify(usu.to_dict()), 200
    else:
        return jsonify({'msg': 'Usuário não encontrado'}), 404

@app.route("/usuarios/<int:id>", methods=['DELETE'])
def del_usuarios(id):
    db = SessionLocal()
    usu = db.query(Usuario).get(id)
    if (usu):
        db.delete(usu)
        db.commit()
        return jsonify({'msg': 'Usuário apagado'}), 204
    else:
        return jsonify({'msg': 'Usuário não encontrado'}), 404

@app.route("/usuarios", methods = ['POST'])
def del_usuario():
    db = SessionLocal()
    data = request.get_json()
    usuario = Usuario(nome=data['nome'], data=data['aniversario'])
    db.add(usuario)
    db.commit()
    return jsonify({'msg': 'Usuário creiado com sucesso!', 'usu':usuario.to_dict()}), 201

@app.route("/usuarios/<int:id>", methods = ['POST'])
def update_usuario(id):
    db = SessionLocal()
    ub = db.query(usuarios).get(id)
    data = request.get_json()
    ub.nome = data['nome']
    ub.data = data['aniversario']
    db.commit()
    return jsonify({'msg': 'Usuário atualizado com sucesso!', 'usu':ub.to_dict()}), 200

