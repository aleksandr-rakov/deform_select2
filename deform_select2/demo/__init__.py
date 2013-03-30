import datetime
import colander
import deform

from colander import iso8601
from deform import ZPTRendererFactory
from deform.i18n import _
from pkg_resources import resource_filename
from pyramid.i18n import get_localizer
from pyramid.threadlocal import get_current_request
from pyramid.view import view_config
from deformdemo import demonstrate, DeformDemo

from deform_select2 import includeme as base_includeme


from deform_select2.widget import Select2Widget
import deform


# Code here exists solely to allow the running of deformdemo.  Use the
# 'includeme' from the __init__.py or similar in your production code,
# not code from here:

search_path = (
        resource_filename('deform_select2', 'templates'),
        resource_filename('deform', 'templates'),
        )


def translator(term):
    return get_localizer(get_current_request()).translate(term)

zpt_renderer = ZPTRendererFactory(search_path, translator=translator)


def includeme(config):
    deform.widget.SelectWidget=Select2Widget
    base_includeme(config)
   
    config.override_asset(
        to_override='deformdemo:templates/main.pt',
        override_with='deform_select2:demo/main.pt',
        )
    
    def onerror(*arg):
        pass
    config.scan('deform_select2.demo', onerror=onerror)

    