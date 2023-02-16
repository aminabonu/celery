from flask import Blueprint
from flask_restx import Api, Resource

from database.models import Card

bp = Blueprint('cards', __name__)
api = Api(bp)

adding_card = api.parser()
adding_card.add_argument('user_id', type=int, required=True)
adding_card.add_argument('card_number', type=int, required=True)
adding_card.add_argument('exp_date', type=str, required=True)
adding_card.add_argument('amount', type=float, required=True)

deleting_card = api.parser()
deleting_card.add_argument('card_number', type=int, required=True)


@api.route('/add-card')
class AddCard(Resource):
    @api.expect(adding_card)
    def post(self):
        response = adding_card.parse_args()
        user_id = response.get('user_id')
        card_number = response.get('card_number')
        exp_date = response.get('exp_date')
        amount = response.get('amount')

        try:
            Card().register_card(card_number, user_id, amount, exp_date)
            return {'status': 1, 'message': 'Card was added'}

        except Exception as e:
            return {'status': 0, 'message': 'Error'}


@api.route('/delete-card')
class DeleteCard(Resource):
    @api.expect(deleting_card)
    def delete(self):
        response = deleting_card.parse_args()
        card_number = response.get('card_number')

        try:
            Card().delete_card(card_number)
            return {'status': 1, 'message': 'Card was deleted'}

        except Exception as e:
            return {'status': 0, 'message': 'Error'}
