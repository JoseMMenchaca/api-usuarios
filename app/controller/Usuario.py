from flask_restful import Resource
from flask import request, jsonify, json
from app.models import db, Usuario, UsuarioSchema
from sqlalchemy import text

usuarios_Schema=UsuarioSchema(many=True)
usuario_Schema = UsuarioSchema()
class UsuarioResource(Resource):
    def get(self):
        usuarios = Usuario.query.all()
        usuarios = usuarios_Schema.dump(usuarios)
        return {"data": usuarios}, 200
    
    def post(self):
        json_data=request.get_json(force=True)

        usuario=Usuario(
            cedula_identidad=json_data['cedula_identidad'],
            nombre=json_data['nombre'],
            primer_apellido=json_data['primer_apellido'],
            segundo_apellido=json_data['segundo_apellido'],
            fecha_nacimiento=json_data['fecha_nacimiento'],
        )

        db.session.add(usuario)
        db.session.commit()

        return {"messagge": 'USUARIO CREADO CORRECTAMENTE'}, 201
    

class UsuarioUpdateResource(Resource):
    def get(self, id=None):
        usuario = Usuario.query.filter_by(id=id).first()
        resultado=usuario_Schema.dump(usuario)

        return {"data": resultado} , 200
    
    def put(self, id=None):
        usuario=Usuario.query.filter_by(id=id).first()
        json_data=request.get_json(force=True)

        usuario.cedula_identidad = json_data.get('cedula_identidad', usuario.cedula_identidad)
        usuario.nombre = json_data.get('nombre', usuario.nombre)
        usuario.primer_apellido = json_data.get('primer_apellido', usuario.primer_apellido)
        usuario.segundo_apellido = json_data.get('segundo_apellido', usuario.segundo_apellido)
        usuario.fecha_nacimiento = json_data.get('fecha_nacimiento', usuario.fecha_nacimiento)

        db.session.commit()

        return {"data":"DATOS ACTUALIZADOS CORRECTAMENTE"} ,200
    
    def delete(self, id=None):
        Usuario.query.filter_by(id=id).delete()
        db.session.commit()
        return {'mensaje':'Usuario Eliminado Correctamente'} , 200
    
class PromedioResource(Resource):
    def get(self):

        promedio = db.session.execute(text('SELECT AVG(EXTRACT(YEAR FROM AGE(NOW(), fecha_nacimiento))) AS promedio from usuario'))
        #results = [tuple(row) for row in promedio]
        for row in promedio:
            json_string = json.dumps(row[0],default=str)
        return {'promedio': json_string}
        

class EstadoResource(Resource):
    def get(self):
        return{
            "nameSystem":"API USER",
            "version"   :"1.0.0",
            "developer" :"JOSE MANUEL MENCHACA ENCINAS",
            "email"     : 'josemenchaca30@gmail.com'
        }