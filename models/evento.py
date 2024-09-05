from sql_alchemy import banco


class EventoModel(banco.Model):
    __tablename__ = 'eventos'

    id = banco.Column(banco.BigInteger, primary_key=True)
    texto = banco.Column(banco.String(160))
    dia = banco.Column(banco.String(40))
    id_cronograma = banco.Column(banco.BigInteger, banco.ForeignKey('cronogramas.id'))

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
        