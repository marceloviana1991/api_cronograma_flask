from flask import Flask
from flask_restful import Api
from resources.cronograma import Cronogramas, CronogramasId

app = Flask(__name__)
api = Api(app)

api.add_resource(Cronogramas, '/cronogramas')
api.add_resource(CronogramasId, '/cronogramas/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
