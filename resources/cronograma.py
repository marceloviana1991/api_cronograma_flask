from flask_restful import Resource, reqparse
from models.cronograma import CronogramaModel


class Cronogramas(Resource):
    def get(self):
        return {'cronogramas': [cronograma.json() for cronograma in CronogramaModel.query.all()]}
    
    def post(sef):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('id')
        argumentos.add_argument('nome')
        dados = argumentos.parse_args()
        id = dados['id']
        if CronogramaModel.find_cronograma(id):
            return {'message': f'Cronograma id: {id} already exists'}, 400
        cronograma_objeto = CronogramaModel(
            id=dados['id'], nome=dados['nome']
        )
        cronograma_objeto.save_cronograma()
        novo_cronograma = cronograma_objeto.json()
        return novo_cronograma, 201
    

class CronogramasId(Resource):
    def get(self, id):
        cronograma_encontrado = CronogramaModel.find_cronograma(id)
        if not cronograma_encontrado:
            return {'message': 'not found'}, 404
        return cronograma_encontrado.json()
    
    def put(self, id):
        cronograma_encontrado = CronogramaModel.find_cronograma(id)
        if not cronograma_encontrado:
            return {'message': 'not found'}, 404
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        dados = argumentos.parse_args()
        cronograma_encontrado.update_cronograma(nome=dados['nome'])
        cronograma_encontrado.save_cronograma()
        return cronograma_encontrado.json()
    
    def delete(self, id):
        cronograma_encontrado = CronogramaModel.find_cronograma(id)
        if cronograma_encontrado:
            cronograma_encontrado.delete_cronograma()
            return {'message': 'deleted'}
        return {'message': 'not found'}, 404
    