from flask_appbuilder.fieldwidgets import (BS3TextFieldWidget,
                                           BS3TextAreaFieldWidget,
                                           Select2Widget)


class BS3TextFieldROWidget(BS3TextFieldWidget):
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(BS3TextFieldROWidget, self).__call__(field, **kwargs)


class BS3TextAreaFieldROWidget(BS3TextAreaFieldWidget):
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(BS3TextAreaFieldWidget, self).__call__(field, **kwargs)


class Select2ROWWidget(Select2Widget):
    def __call__(self, *args, **kwargs):
        kwargs['readonly'] = 'true'
        return super(Select2Widget, self).__call__(*args, **kwargs)