from flask import render_template
from app import appbuilder, db
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app.models import Category, Item

from flask_appbuilder.fieldwidgets import BS3TextAreaFieldWidget, TextField


"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""


class ItemModelView(ModelView):
    datamodel = SQLAInterface(Item)

    label_columns = {'category': 'Category'}
    list_columns = ['title', 'description', 'category']

    show_fieldsets = [
                        (
                            'Summary',
                            {'fields': ['title', 'category']}
                        ),
                     ]

    edit_form_extra_fields = {'description':    TextField('Provide a description',
                                                description='Item description',
                                                widget=BS3TextAreaFieldWidget())}

    add_form_extra_fields = {'description': TextField('Provide a description',
                                                       description='Item description',
                                                       widget=BS3TextAreaFieldWidget())}


class CategoryModelView(ModelView):
    datamodel = SQLAInterface(Category)
    related_views = [ItemModelView]


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
