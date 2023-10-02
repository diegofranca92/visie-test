import ormar
from config import database, metadata

class Person(ormar.Model):
    class Meta: 
        metadata = metadata
        database = database
        tablename = 'pessoas'
    id_pessoa: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    rg: str = ormar.String(max_length=30)
    cpg: str = ormar.String(max_length=30)
    data_nascimento: str = ormar.String(max_length=15)
    data_admissao: str = ormar.String(max_length=15)
    funcao: str = ormar.String(max_length=100)