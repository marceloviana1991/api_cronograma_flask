from sql_alchemy import banco


class CronogramaModel(banco.Model):
    __tablename__ = 'cronogramas'

    id = banco.Column('id',banco.BigInteger, primary_key=True)
    nome = banco.Column('nome', banco.String(80))

    def __init__(self, id, nome):
        self.id = int(id)
        self.nome = nome

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
    
    @classmethod
    def find_cronograma(cls, id):
        cronograma = cls.query.filter_by(id=id).first()
        if cronograma:
            return cronograma
        return None
    
    def save_cronograma(self):
        banco.session.add(self)
        banco.session.commit()
    