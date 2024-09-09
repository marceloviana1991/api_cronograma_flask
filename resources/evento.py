from flask_restful import Resource, reqparse
from models.evento import EventoModel
from models.cronograma import CronogramaModel


class Eventos(Resource):
    def get(self):
        return {'eventos': [evento.json() for evento in EventoModel.query.all()]}
    
    def post(self):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('id')
        argumentos.add_argument('texto')
        argumentos.add_argument('dia')
        argumentos.add_argument('id_cronograma')
        dados = argumentos.parse_args()
        id = dados['id']
        id_cronograma = dados['id_cronograma']
        if EventoModel.find_evento(id):
            return {'message': f'Evento id: {id} already exists'}, 400
        cronograma_encontrado = CronogramaModel.find_cronograma(id_cronograma)
        if not cronograma_encontrado:
            return {'message': f'Cronogramada id: {id} not found'}, 404
        evento_objeto = EventoModel(
            id=dados['id'],
            texto=dados['texto'],
            dia=dados['dia'],
            id_cronograma=dados['id_cronograma']
        )
        cronograma_encontrado.eventos.append(evento_objeto)
        evento_objeto.save_evento()
        novo_evento = evento_objeto.json()
        return novo_evento, 201
    

class EventosId(Resource):
    def get(self, id):
        evento_encontrado = EventoModel.find_evento(id)
        if not evento_encontrado:
            return {'message': 'not found'}, 404
        return evento_encontrado.json()
    
    def put(self, id):
        evento_encontrado = EventoModel.find_evento(id)
        if not evento_encontrado:
            return {'message': 'not found'}, 404
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('texto')
        argumentos.add_argument('dia')
        dados = argumentos.parse_args()
        evento_encontrado.update_evento(
            texto=dados['texto'],
            dia=dados['dia']
        )
        evento_encontrado.save_evento()
        return evento_encontrado.json()
    
    def delete(self, id):
        evento_encontrado = EventoModel.find_evento(id)
        if evento_encontrado:
            evento_encontrado.delete_evento()
            return {'message': 'deleted'}
        return {'message': 'not found'}, 404
        