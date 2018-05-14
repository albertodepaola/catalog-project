from flask_appbuilder import IndexView


class CatalogIndexView(IndexView):
    index_template = 'index.html'