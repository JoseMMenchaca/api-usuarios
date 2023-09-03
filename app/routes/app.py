from flask import Blueprint
from flask_restful import Api
from app.controller.Usuario import UsuarioResource, UsuarioUpdateResource, PromedioResource, EstadoResource

bp=Blueprint('api',__name__)
api=Api(bp)

api.add_resource(UsuarioResource, '/usuario')
api.add_resource(UsuarioUpdateResource,'/usuario/<int:id>')
api.add_resource(PromedioResource,'/promedio-edad')
api.add_resource(EstadoResource,'/estado')
