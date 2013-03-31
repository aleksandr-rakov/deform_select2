from deform.widget import SelectWidget,TextInputWidget

class Select2Widget(SelectWidget):
    template = 'select2'
    requirements = (('select2', None), )
    placeholder=''
    allowClear=False

class Select2TagsTextWidget(TextInputWidget):
    template = 'select2tagstext'
    requirements = (('select2', None), )
    tags=["red", "green", "blue"]
