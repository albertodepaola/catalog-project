import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
from app.index import CatalogIndexView


"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=CatalogIndexView)

# import at end of file because of flask appbuilder quirk
from app import views
