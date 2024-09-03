from flask import Flask
from flask_restful import Api
from resources.cronograma import Cronogramas, CronogramaIdUrl, Cronograma

app = Flask(__name__)
api = Api(app)

api.add_resource(Cronogramas, '/cronogramas')
api.add_resource(CronogramaIdUrl, '/cronogramas/<int:id>')
api.add_resource(Cronograma, '/cronogramas')

if __name__ == '__main__':
    app.run(debug=True)
