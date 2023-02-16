from flask import Blueprint
from flask_restx import Api, Resource

from database.models import TransfersP2P

# bp = Blueprint('monitoring', __name__)
# api = Api(bp)

from users import api

monitoring_model = api.parser()
monitoring_model.add_argument('card_number_or_all', type=str, required=True)


@api.route('/expenses')
class GetUserMonitoring(Resource):
    @api.expect(monitoring_model)
    def get(self):
        card_number = monitoring_model.parse_args()

        result = TransfersP2P().monitoring_pays(card_number.get('card_number'))
        if result:
            return {'status': 1, 'message': result}

        return {'status': 0, 'message': 'Нету ничего'}
