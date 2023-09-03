from app import db, ma
from marshmallow import Schema, fields, pre_load, validate
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    cedula_identidad = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(256),nullable=False)
    primer_apellido = db.Column(db.String(256),nullable=True)
    segundo_apellido = db.Column(db.String(256),nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return "<Usuario(cedula_identidad='%s', nombre='%s', primer_apellido='%s', segundo_apellido='%s', fecha_nacimiento='%s')>" % (
            self.cedula_identidad,
            self.nombre,
            self.primer_apellido,
            self.segundo_apellido,
            self.fecha_nacimiento,
        )



class UsuarioSchema(ma.Schema):
    class Meta:
        ordered = True
    id = fields.Integer(dump_only=True)
    cedula_identidad = fields.String(required=True, error_messages={"required": "campo Cedula de Identidad es requerido."})
    nombre = fields.String(required=True, error_messages={"required": "campo nombre es requerido."})
    primer_apellido = fields.String(required=False)
    segundo_apellido = fields.String(required=True, error_messages={"required": "campo segundo apellido es requerido."})
    fecha_nacimiento = fields.String(required=True, error_messages={"required": "campo fecha de nacimiento es requerido."})
