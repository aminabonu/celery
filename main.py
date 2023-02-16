from flask import Flask

from database.models import db
from flask_migrate import Migrate

import business
import users

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/pay'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pay'
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(users.bp)
app.register_blueprint(business.bp)

# app.register_blueprint(users.cards.bp, url_prefix='/card')
# app.register_blueprint(users.monitoring.bp, url_prefix='/monitoring')
# app.register_blueprint(users.registration.bp, url_prefix='/registration')
# app.register_blueprint(users.service_payments.bp, url_prefix='/payments')
# app.register_blueprint(users.transfers.bp, url_prefix='/transfer')
#
#
# app.register_blueprint(business.cabinet.bp, url_prefix='/cabinet')
# app.register_blueprint(business.income_business.bp, url_prefix='/income')
# app.register_blueprint(business.invoice_business.bp, url_prefix='/invoice')


@app.route('/')
def index():
    return 'Main page'
