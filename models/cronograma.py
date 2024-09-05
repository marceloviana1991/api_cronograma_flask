from sql_alchemy import banco


class CronogramaModel(banco.Model):
    __tablename__ = 'cronogramas'

    id = banco.Column(banco.BigInteger, primary_key=True)
    nome = banco.Column(banco.String(80))

    def __init__(self, id, nome):
        self.id = int(id)
        self.nome = nome

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
    