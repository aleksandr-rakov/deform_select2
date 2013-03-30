from deform.widget import SelectWidget

class Select2Widget(SelectWidget):
    template = 'select2'
    requirements = (('select2', None), )
    placeholder=''
    allowClear=False
