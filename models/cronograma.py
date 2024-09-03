
class CronogramaModel:
    def __init__(self, id, nome):
        self.id = int(id)
        self.nome = nome

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
    