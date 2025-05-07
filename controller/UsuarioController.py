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