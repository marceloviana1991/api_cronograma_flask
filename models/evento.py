
class EventoModel:
    def __init__(self, id, texto, dia, id_cronograma):
        self.id = int(id)
        self.texto = texto
        self.dia = dia
        self.id_cronograma = int(id_cronograma)

    def json(self):
        return {
            'id': self.id,
            'texto': self.texto,
            'dia': self.dia,
            'id_crograma': self.id_cronograma
        }
        