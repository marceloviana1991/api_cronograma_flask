from flask_restful import Resource, reqparse
from models.cronograma import CronogramaModel


class Cronogramas(Resource):
    def get(self):
        return {'cronogramas': [cronograma.json() for cronograma in CronogramaModel.query.all()]}
    
    def post(sef):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('id', type=int)
        argumentos.add_argument('nome', required=True, help="The field 'nome' cannot is null")
        dados = argumentos.parse_args()
        id = dados['id']
        if CronogramaModel.find_cronograma(id):
            return {'message': f'Cronograma id: {id} already exists'}, 400
        cronograma_objeto = CronogramaModel(
            id=dados['id'], nome=dados['nome']
        )
        try:
            cronograma_objeto.save_cronograma()
        except:
            return {'message': 'An internal error'}, 500
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
        try:
            cronograma_encontrado.save_cronograma()
        except:
            return {'message': 'An internal error'}, 500
        return cronograma_encontrado.json()
    
    def delete(self, id):
        cronograma_encontrado = CronogramaModel.find_cronograma(id)
        if cronograma_encontrado:
            try:
                cronograma_encontrado.delete_cronograma()
            except:
                return {'message': 'An internal error'}, 500
            return {'message': 'deleted'}
        return {'message': 'not found'}, 404
    