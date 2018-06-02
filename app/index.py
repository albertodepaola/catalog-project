from flask import render_template
from flask_appbuilder import IndexView, expose, BaseView
from app.models import Item, Category


class CatalogIndexView(IndexView):
    # index_template = 'index.html'
    # base_template = 'asd'

    @expose('/')
    def index(self):
        latest_items = self.get_latest()
        categories = self.appbuilder.get_session.query(Category).order_by(Category.name).all()

        return render_template('index.html', testVar='test', items=latest_items, appbuilder=self.appbuilder, categories=categories)

    def get_latest(self):
        return self.appbuilder.get_session.query(Item).order_by(Item.id.desc()).limit(10).all()




