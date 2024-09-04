from flask import Flask
from flask_restful import Api
from resources.cronograma import Cronogramas, CronogramasId
from resources.evento import Eventos, EventosId

app = Flask(__name__)
api = Api(app)

api.add_resource(Cronogramas, '/cronogramas')
api.add_resource(CronogramasId, '/cronogramas/<int:id>')

api.add_resource(Eventos, '/eventos')
api.add_resource(EventosId, '/eventos/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
