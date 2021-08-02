
import json
import logging

from mkdocs.plugins import BasePlugin

log = logging.getLogger("mkdocs.plugins." + __name__)

class ComputePods(BasePlugin) :

  def __init__(self):
    log.info("Initialized ComputePods plugin")

  def on_template_context(self, context, template_name, config) :
    new_base_url = context['base_url'] + '/../'
    new_base_url = new_base_url.replace('//', '/')
    context['base_url'] = new_base_url
    return context
