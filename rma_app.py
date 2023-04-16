from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

RMA_Players = {
    0:{'name':'Carlo Ancelotti'},
    1:{'name':'Thibaut Courtois'},
    2:{'name':'Daniel Carvajal'},
    3:{'name':'Eder Militao'},
    4:{'name':'David Alaba'},
    5:{'name':'Jesus Vallejo'},
    6:{'name':'Nacho Fernandez'},
    7:{'name':'Eden Hazard'},
    8:{'name':'Toni Kross'},
    9:{'name':'Karim Banzema'},
    10:{'name':'Luka Modric'},
    11:{'name':'Marco Asensio'},
    12:{'name':'Eduardo Camavinga'},
    13:{'name':'Andriy Lunin'},
    14:{'name':'brak zawodnika'},
    15:{'name':'Federico Valverde'},
    16:{'name':'Alvaro Odriozola'},
    17:{'name':'Lucas Vazquez'},
    18:{'name':'Aurelien Tchouameni'},
    19:{'name':'Daniel Ceballos'},
    20:{'name':'Vinicius Junior'},
    21:{'name':'Rodrygo Goes'},
    22:{'name':'Antonio Rudiger'},
    23:{'name':'Ferland Mendy'}
    }

class Players(Resource):
    def get(self):
        return RMA_Players

    def post(self):
        data = request.json
        PlayerId = len(RMA_Players.keys()) +1
        RMA_Players[PlayerId] = {'name':data['name'] }
        return RMA_Players

class Player(Resource):
    def get(self, pk):
        return RMA_Players[pk]

    def put(self, pk):
        data = request.json
        RMA_Players[pk]['name'] = data['name']
        return RMA_Players

    def delete(self, pk):
        del RMA_Players[pk]
        return RMA_Players

        
api.add_resource(Players, '/')        
api.add_resource(Player, '/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)