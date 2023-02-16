from flask import Blueprint
from flask_restx import Api, Resource

from database.models import Payment, Business

# bp = Blueprint('income_business', __name__)
# api = Api(bp)

from business import api

income_from_business = api.parser()
income_from_business.add_argument('user_id', type=int, required=True)


@api.route('/income')
class GettingBusinessIncome(Resource):
    @api.expect(income_from_business)
    def get(self):
        args = income_from_business.parse_args()
        user_id = args.get('user_id')

        business_to_get = Business.query.get(user_id)
        incomes = Payment().monitor_pays(business_to_get.business_card)

        return {'status': 1, 'message': incomes}
