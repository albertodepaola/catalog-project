from flask import render_template, make_response
from flask_appbuilder import IndexView, expose, BaseView
from app.models import Item, Category
import json


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

    @expose("/catalog.json")
    def json(self):

        categories = []

        for category in self.appbuilder.get_session.query(Category).all():

            copy = category.to_json()

            items = self.appbuilder.get_session.query(Item).filter(Item.category_id == category.id).all()

            items_json = []
            for item in items:
                items_json.append(item.to_json())

            copy['Item'] = items_json

            categories.append(copy)

        category_as_json = {'Category': categories}

        response = make_response(json.dumps(category_as_json), 200)
        response.headers['Content-Type'] = 'application/json'
        return response




