from flask_restful import Resource, reqparse
from models.cronograma import CronogramaModel


cronogramas = [
    {"id" : 1, 'nome':'atividade fisica'},
    {"id" : 2, 'nome':'atividades domesticas'}
]


class Cronogramas(Resource):
    def get(self):
        return {'cronogramas': cronogramas}
    

class CronogramaIdUrl(Resource):
    def get(self, id):
        cronograma_encontrado = [cronograma for cronograma in cronogramas if cronograma['id']==id]
        if not cronograma_encontrado:
            return {'message': 'not found'}, 404
        return cronograma_encontrado[0]
    
    def put(self, id):
        cronograma_encontrado = [cronograma for cronograma in cronogramas if cronograma['id']==id]
        if not cronograma_encontrado:
            return {'message': 'not found'}, 404
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        dados = argumentos.parse_args()
        cronograma_encontrado[0]['nome'] = dados['nome']
        return cronograma_encontrado[0]
    
    def delete(self, id):
        global cronogramas
        cronogramas = [cronograma for cronograma in cronogramas if cronograma['id']!=id]
        return {'message': 'deleted'}
    
    
class Cronograma(Resource):
    def post(sef):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('id')
        argumentos.add_argument('nome')
        dados = argumentos.parse_args()
        cronograma_objeto = CronogramaModel(
            id=dados['id'], nome=dados['nome']
        )
        novo_cronograma = cronograma_objeto.json()
        cronogramas.append(novo_cronograma)
        return novo_cronograma, 201