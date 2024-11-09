from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dbhotel_fillscreen:79455f36812f1a2a169ad8b61a480452cb0e4c17@9780d.h.filess.io:3305/dbhotel_fillscreen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()