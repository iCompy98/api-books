from flask import  Blueprint
from project.src import control

routes = Blueprint('routes', __name__)

routes.add_url_rule('/','main', control.index,methods=['GET'])
routes.add_url_rule('/contacts','Obtener todos los contactos', control.allContacts, methods=['GET'])
routes.add_url_rule('/contacts/<contact_id>','Obtener datos de un contacto', control.getContact, methods=['GET'])
routes.add_url_rule('/contacts/<contact_id>','Eliminar un contacto', control.deleteContact, methods=['DELETE'])

