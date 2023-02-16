from flask import Blueprint
from flask_restx import Api

bp = Blueprint('users', __name__, url_prefix='/users')
api = Api(bp)

from . import cards, monitoring, registration, service_payments, transfers
