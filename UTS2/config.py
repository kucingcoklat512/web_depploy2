from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector:/dbhotel2_headedtall:d000b1fc0c1d13802ec156ab36cdf4fb9974c428@glcpd.h.filess.io:3305/dbhotel2_headedtall'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
