from flask import Blueprint
from flask_restx import Api, Resource

from database.models import ServiceType

# bp = Blueprint('cabinet', __name__)
# api = Api(bp)

from business import api

register_service = api.parser()
register_service.add_argument('service_name', type=str, required=True)
register_service.add_argument('service_type', type=str, required=True)


@api.route('/add-service')
class RegService(Resource):
    @api.expect(register_service)
    def post(self):
        response = register_service.parse_args()
        service_name = response.get('service_name')
        service_type = response.get('service_type')

        try:
            ServiceType().register_service(service_name, service_type)

            return {'status': 1, 'message': 'Service was added'}

        except Exception as e:
            return {'status': 0, 'message': 'Error'}

