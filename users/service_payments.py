from flask import Blueprint
from flask_restx import Api, Resource

from database.models import Payment

# bp = Blueprint('service_payments', __name__)
# api = Api(bp)

from users import api

service_payment_model = api.parser()
service_payment_model.add_argument('service_type_name', type=str, required=True)
service_payment_model.add_argument('amount', type=float, required=True)
service_payment_model.add_argument('from_card', type=int, required=True)


@api.route('pay-service')
class ServicePayment(Resource):
    @api.expect(service_payment_model)
    def post(self):
        response = service_payment_model.parse_args()
        service_type_name = response.get('service_type_name')
        from_card = response.get('from_card')
        amount = response.get('amount')

        try:
            Payment().create_payment(from_card, amount, service_type_name)

            return {'status': 1, 'message': 'Упешно оплачено'}

        except Exception as e:
            return {'status': 1, 'message': str(e)}
