from flask import Blueprint
from flask_restx import Api, Resource

from database.models import Payment, User, Card

# bp = Blueprint('invoice', __name__)
# api = Api(bp)


from business import api

invoice_from_business = api.parser()
invoice_from_business.add_argument('service_id', type=int, required=True)
invoice_from_business.add_argument('service_name', type=str, required=True)
invoice_from_business.add_argument('amount', type=float, required=True)
invoice_from_business.add_argument('phone_number', type=str, required=True)


@api.route('/send-invoice')
class SendingInvoiceBusiness(Resource):
    @api.expect(invoice_from_business)
    def post(self):
        response = invoice_from_business.parse_args()
        service_id = response.get('service_id')
        service_name = response.get('service_name')
        amount = response.get('amount')
        phone_number = response.get('phone_number')

        user_id = User.query.filter_by(user_phone_number=phone_number).first().id
        card_number = Card.query.filter_by(user_id=user_id).first().card_number

        payment = Payment().create_payment(card_number, amount, service_name)

        if payment:
            return {'status': 1, 'message': 'Done!'}

        return {'status': 0, 'message': 'Not enough money'}
