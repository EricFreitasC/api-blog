from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configurações inicias
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.rrvbonysabahqyzznwgm:c9iY3$vwcKWHX4D@aws-0-sa-east-1.pooler.supabase.com:6543/postgres'

db = SQLAlchemy(app)
db: SQLAlchemy

class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

with app.app_context():
    db.drop_all()
    db.create_all()
    autor = Autor(nome='eric', email='eric@gmail.com',
                    senha='senha123', admin=True)
    db.session.add(autor)
    db.session.commit()
