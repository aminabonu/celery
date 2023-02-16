# from flask import Blueprint
from flask_restx import Api, Resource

import random

from database.models import TransfersP2P

# bp = Blueprint('transfers', __name__)
# api = Api(bp)

from users import api

transfer_model = api.parser()
transfer_model.add_argument('user_from_id', type=int, required=True)
transfer_model.add_argument('user_from_card', type=int, required=True)
transfer_model.add_argument('to_card', type=int, required=True)
transfer_model.add_argument('amount', type=float, required=True)
transfer_model.add_argument('verify_code', type=int, required=True)

veryfi_model = api.parser()
veryfi_model.add_argument('card_number', type=str, required=True)

test_ver = {}


@api.route('/transfer-money')
class Transfers(Resource):
    @api.expect(transfer_model)
    def post(self):
        args = transfer_model.parse_args()
        user_from_id = args.get('user_form_id')
        user_from_card = args.get('user_form_card')
        to_card = args.get('to_card')
        amount = args.get('amount')
        code = args.get('veryfi_code')

        if test_ver[user_from_card] == code:

            result = TransfersP2P().create_payment(user_from_id, user_from_card, to_card, amount)

            return {'status': 1, 'message': result}

        return {'status': 0, 'message': 'За тобой уже выехали'}


@api.route('/get-verify-code')
class GetVeryfi(Resource):
    @api.expect(veryfi_model)
    def get(self):
        args = veryfi_model.parse_args()
        card_number = args.get('card_number')

        veryfi_code = random.randint(1212, 9999)
        test_ver[card_number] = veryfi_code

        return {'status': 1, 'message': veryfi_code}