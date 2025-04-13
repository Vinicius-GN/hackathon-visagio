from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Colaborador(db.Model):
    __tablename__ = 'colaboradores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    avaliacoes = db.relationship('Avaliacao', backref='colaborador', cascade="all, delete")

class Avaliacao(db.Model):
    __tablename__ = 'avaliacoes'
    id = db.Column(db.Integer, primary_key=True)
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaboradores.id'), nullable=False)
    data_avaliacao = db.Column(db.Date, nullable=False)
    notas = db.relationship('Nota', backref='avaliacao', cascade="all, delete")

class Criterio(db.Model):
    __tablename__ = 'criterios'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum('comportamental', 'execucao'), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    notas = db.relationship('Nota', backref='criterio', cascade="all, delete")

class Nota(db.Model):
    __tablename__ = 'notas'
    id = db.Column(db.Integer, primary_key=True)
    avaliacao_id = db.Column(db.Integer, db.ForeignKey('avaliacoes.id'), nullable=False)
    criterio_id = db.Column(db.Integer, db.ForeignKey('criterios.id'), nullable=False)
    nota = db.Column(db.Numeric(2,1), nullable=False)
    justificativa = db.Column(db.Text)
