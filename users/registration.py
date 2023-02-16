from flask import Blueprint
from flask_restx import Api, Resource

from database.models import User

bp = Blueprint('registration', __name__)
api = Api(bp)

reging_user = api.parser()
reging_user.add_argument('username', type=str, required=True)
reging_user.add_argument('phone_number', type=str, required=True)


@api.route('/register')
class RegisterUser(Resource):
    @api.expect(reging_user)
    def post(self):
        response = reging_user.parse_args()
        username = response.get('username')
        phone_number = response.get('phone_number')

        try:
            User().register_user(phone_number, username)
            return {'status': 1, 'message': 'User was added'}

        except Exception as e:
            return {'status': 0, 'message': 'Error'}
