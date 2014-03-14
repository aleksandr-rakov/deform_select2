from deform.widget import SelectWidget, TextInputWidget, Widget
from colander import null

class Select2Widget(SelectWidget):
    template = 'select2'
    requirements = (('select2', None), )
    placeholder=''
    allowClear=False

class Select2TagsTextWidget(TextInputWidget):
    template = 'select2tagstext'
    readonly_template = 'readonly/textinput'
    requirements = (('select2', None), )
    tags=tuple()

class Select2TagsListWidget(Widget):
    template = 'select2tagslist'
    readonly_template = 'readonly/textinput'
    null_value = tuple()
    tags=tuple()

    def serialize(self, field, cstruct, **kw):
        if cstruct in (null, None):
            cstruct = self.null_value
        readonly = kw.get('readonly', self.readonly)
        template = readonly and self.readonly_template or self.template
        tmpl_values = self.get_template_values(field, cstruct, kw)
        return field.renderer(template, **tmpl_values)

    def deserialize(self, field, pstruct):
        if pstruct in (null, self.null_value):
            return self.null_value
        return [x.strip() for x in pstruct.split(',')]

class Select2RemoteWidget(SelectWidget):
    template = 'select2remote'
    requirements = (('select2', None), )
    placeholder=''
    allowClear=False

    def get_name(self,cstruct):
        if hasattr(self,'get_name_callback'):
            return self.get_name_callback(cstruct)
        else:
            return cstruct
