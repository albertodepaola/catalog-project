from flask import render_template, session
from app import appbuilder, db
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app.models import Category, Item
from flask_appbuilder.fieldwidgets import BS3TextAreaFieldWidget, TextField
from app.widgets import BS3TextFieldROWidget, BS3TextAreaFieldROWidget


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

    show_fieldsets = [
        (
            'Summary',
            {'fields': ['title', 'category']}
        ),
    ]

    edit_form_extra_fields = {'description': TextField('Provide a description',
                                                       description='Item description',
                                                       widget=BS3TextAreaFieldWidget())}

    add_form_extra_fields = {'description': TextField('Provide a description',
                                                      description='Item description',
                                                      widget=BS3TextAreaFieldWidget())}

    def pre_add(self, item):
        user_id = session['user_id']
        item.user_id = user_id

    def pre_update(self, item):
        check_logged_user(item)

    def prefill_form(self, form, pk):
        # Checks if logged user is the creator
        category = self.datamodel.get(pk)
        user_id = session['user_id']
        if category.user_id != int(user_id):
            form.title.widget = BS3TextFieldROWidget()
            form.description.widget = BS3TextAreaFieldROWidget()
            # form.category.widget = Select2ROWWidget()

    def pre_delete(self, item):
        # checks if user logged is the creator
        check_logged_user(item)


class CategoryModelView(ModelView):
    datamodel = SQLAInterface(Category)
    related_views = [ItemModelView]

    visible_columns = ['name']

    add_columns = visible_columns
    edit_columns = visible_columns

    def pre_add(self, item):
        user_id = session['user_id']
        item.user_id = user_id

    def pre_update(self, item):
        check_logged_user(item)

    def prefill_form(self, form, pk):
        # Checks if logged user is the creator
        category = self.datamodel.get(pk)
        user_id = session['user_id']
        if category.user_id != int(user_id):
            form.name.widget = BS3TextFieldROWidget()

    def pre_delete(self, item):
        # checks if user logged is the creator
        check_logged_user(item)


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


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
