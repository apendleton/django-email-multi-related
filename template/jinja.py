# -*- coding: utf-8 -*-
# http://jinja.pocoo.org/docs/extensions/#module-jinja2.ext

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import default_storage

from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.exceptions import TemplateSyntaxError
from coffin.template.library import Library


class EmailMultiRelatedFileEmbeddedExtension(Extension):
    tags = set(['email_embedded_media'])

    def __init__(self, environment):
        super(EmailMultiRelatedFileEmbeddedExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(
            email_object_instance=None
        )

    def parse(self, parser):
        lineno = parser.stream.next().lineno
        path = parser.parse_expression()
        return nodes.Output([
            self.call_method('_render', [path, nodes.Name('_current_app', 'load')]),
        ]).set_lineno(lineno)

    def _render(self, path, caller):
        return 'cid:' + self.environment.email_object_instance.attach_related_file(default_storage.path(path))


# nicer import names
email_embedded_media = EmailMultiRelatedFileEmbeddedExtension

register = Library()
register.tag(email_embedded_media)