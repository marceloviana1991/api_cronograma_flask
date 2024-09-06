from sql_alchemy import banco


class EventoModel(banco.Model):
    __tablename__ = 'eventos'

    id = banco.Column('id', banco.BigInteger, primary_key=True)
    texto = banco.Column('texto', banco.String(160))
    dia = banco.Column('dia', banco.String(40))
    id_cronograma = banco.Column('id_cronograma', banco.BigInteger, banco.ForeignKey('cronogramas.id'))

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
    
    @classmethod
    def find_evento(cls, id):
        evento = cls.query.filter_by(id=id).first()
        if evento:
            return evento
        return None
    
    def save_evento(self):
        banco.session.add(self)
        banco.session.commit()
        