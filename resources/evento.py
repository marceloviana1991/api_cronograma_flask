from flask_restful import Resource, reqparse
from models.evento import EventoModel


eventos = [
    {'id': 1, 'texto': 'fazer caminhada', 'dia': 'quarta-feira', 'id_cronograma': 1},
    {'id': 2, 'texto': 'lavar a cozina', 'dia': 'sabado', 'id_cronograma': 2}
]


class Eventos(Resource):
    def get(self):
        return {'eventos': eventos}
    
    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('id')
        argumentos.add_argument('texto')
        argumentos.add_argument('dia')
        argumentos.add_argument('id_cronograma')
        dados = argumentos.parse_args()
        evento_objeto = EventoModel(
            id=dados['id'],
            texto=dados['texto'],
            dia=dados['dia'],
            id_cronograma=dados['id_cronograma']
        )
        novo_evento = evento_objeto.json()
        eventos.append(novo_evento)
        return novo_evento, 201
    

class EventosId(Resource):
    def get(self, id):
        evento_encontrado = [evento for evento in eventos if evento['id']==id]
        if not evento_encontrado:
            return {'message': 'not found'}, 404
        return evento_encontrado[0]
    
    def put(self, id):
        evento_encontrado = [evento for evento in eventos if evento['id']==id]
        if not evento_encontrado:
            return {'message': 'not found'}, 404
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('texto')
        argumentos.add_argument('dia')
        dados = argumentos.parse_args()
        evento_encontrado[0]['texto'] = dados['texto']
        evento_encontrado[0]['dia'] = dados['dia']
        return evento_encontrado[0]
    
    def delete(self, id):
        global eventos
        eventos = [evento for evento in eventos if evento['id']!=id]
        return {'message': 'deleted'}
