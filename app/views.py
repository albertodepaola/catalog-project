from flask import render_template, session, make_response
from app import appbuilder, db
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, expose
from app.models import Category, Item
from flask_appbuilder.fieldwidgets import BS3TextAreaFieldWidget, TextField
from app.widgets import BS3TextFieldROWidget, BS3TextAreaFieldROWidget
import json


# Method used to check if the logged in user is the author of the record.
# If it isn't, it raises an error.
def check_logged_user(item):
    user_id = session['user_id']
    if item.user_id != int(user_id):
        raise ValueError("Cannot modify this record, created by another user")


class ItemModelView(ModelView):
    datamodel = SQLAInterface(Item)

    label_columns = {'category': 'Category'}
    list_columns = ['title', 'description', 'category']
    visible_columns = ['title', 'description', 'category']

    add_columns = visible_columns
    edit_columns = visible_columns
    show_columns = visible_columns

    show_fieldsets = [
        (
            'Summary',
            {'fields': ['title', 'description', 'category']}
        ),
    ]

    edit_form_extra_fields = {'description':
                              TextField('Provide a description',
                                        description='Item description',
                                        widget=BS3TextAreaFieldWidget())}

    add_form_extra_fields = {'description':
                             TextField('Provide a description',
                                       description='Item description',
                                       widget=BS3TextAreaFieldWidget())}

    # adds custom endpoint to query items by name
    @expose('/<name>')
    def detail(self, name):
        item = self.appbuilder\
            .get_session.query(Item)\
            .filter(Item.title == name)\
            .one_or_none()
        return render_template('item.html',
                               appbuilder=self.appbuilder,
                               item=item)

    @expose('/<filter_id>')
    def as_json(self, filter_id):
        item = self.appbuilder\
            .get_session.query(Item)\
            .filter(Item.id == filter_id) \
            .one_or_none()
        if item is None:
            item_json = json.dumps({})
        else:
            item_json = json.dumps(item.to_json())
        response = make_response(item_json, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    def pre_add(self, item):
        user_id = session['user_id']
        item.user_id = user_id

    def pre_update(self, item):
        check_logged_user(item)

    def prefill_form(self, form, pk):
        # checks if the logged in user is the author,
        # if it's not, shows data readonly
        category = self.datamodel.get(pk)
        user_id = session['user_id']
        if category.user_id != int(user_id):
            form.title.widget = BS3TextFieldROWidget()
            form.description.widget = BS3TextAreaFieldROWidget()
            # TODO create a readonly widget that works correctly
            # form.category.widget = Select2ROWWidget()

    def pre_delete(self, item):
        check_logged_user(item)


class CategoryModelView(ModelView):
    datamodel = SQLAInterface(Category)
    related_views = [ItemModelView]

    visible_columns = ['name']

    add_columns = visible_columns
    edit_columns = visible_columns

    # adds custom endpoint to query categories by name
    @expose('/<name>')
    def detail(self, name):
        category = self.appbuilder\
            .get_session.query(Category)\
            .filter(Category.name == name) \
            .one_or_none()
        return render_template('category.html',
                               appbuilder=self.appbuilder,
                               category=category)

    @expose('/<filter_id>')
    def as_json(self, filter_id):
        category = self.appbuilder\
            .get_session.query(Category)\
            .filter(Category.id == filter_id) \
            .one_or_none()
        if category is None:
            category_json = json.dumps({})
        else:
            category_json = json.dumps(category.to_json())
        response = make_response(category_json, 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    def pre_add(self, item):
        user_id = session['user_id']
        item.user_id = user_id

    def pre_update(self, item):
        check_logged_user(item)

    def prefill_form(self, form, pk):
        # checks if the logged in user is the author,
        # if it's not, shows data readonly
        category = self.datamodel.get(pk)
        user_id = session['user_id']
        if category.user_id != int(user_id):
            form.name.widget = BS3TextFieldROWidget()

    def pre_delete(self, item):
        check_logged_user(item)


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
                           base_template=appbuilder.base_template,
                           appbuilder=appbuilder), \
           404

db.create_all()

appbuilder.add_view(CategoryModelView,
                    "List Categories",
                    icon="fa-folder-open-o",
                    category="Catalog",
                    category_icon="fa-envelope")
appbuilder.add_view(ItemModelView,
                    "List Items",
                    icon="fa-envelope",
                    category="Catalog")
