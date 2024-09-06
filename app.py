from flask import Flask
from flask_restful import Api
from resources.cronograma import Cronogramas, CronogramasId
from resources.evento import Eventos, EventosId
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


caminho_arquivo = "instance/banco.db"
@app.before_request
def cria_banco():
        if not(os.path.exists(caminho_arquivo)):
            banco.create_all()
        


api.add_resource(Cronogramas, '/cronogramas')
api.add_resource(CronogramasId, '/cronogramas/<int:id>')

api.add_resource(Eventos, '/eventos')
api.add_resource(EventosId, '/eventos/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
