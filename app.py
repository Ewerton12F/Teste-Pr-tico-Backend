import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# INIT APP ---------------------------------------------------------------------
app = Flask(__name__)

# DATABASE ---------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ewertonfreitas:ZXdlcnRvbmZy@jobs.visie.com.br/ewertonfreitas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# INIT DB ----------------------------------------------------------------------
db = SQLAlchemy(app)

"""
# INIT MA ----------------------------------------------------------------------
ma = Marshmallow(app)
"""
""" 
# PESSOA CLASS/MODEL -----------------------------------------------------------
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable=False)
    rg = db.Column(db.Integer(), nullable=False)
    cpf = db.Column(db.Integer(), nullable=False)
    data_nascimento = db.Column(db.Date(), nullable=False)
    data_admissao = db.Column(db.Date(), nullable=False)
    funcao = db.Column(db.String(100), nullable=True)
    

    def __init__(self, nome, rg, cpf, data_nascimento, data_admissao, funcao):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao
        self.funcao = funcao
"""
""" 
# PESSOA SCHEMA ----------------------------------------------------------------
class PessoaSchema(ma.Schema):
    class Meta:
        fields = ('nome', 'data_admissao')
# INIT SCHEMA ------------------------------------------------------------------
pessoa_schema = PessoaSchema()
pessoas_schema = PessoaSchema(many=True)
"""

# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query('1').from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is broken.</h1>'
        
# RETRIEVE ---------------------------------------------------------------------

# RUN SERVER -------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# RUN SERVER /