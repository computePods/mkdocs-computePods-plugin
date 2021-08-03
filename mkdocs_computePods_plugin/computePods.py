
import json
import logging

from mkdocs.plugins import BasePlugin

log = logging.getLogger("mkdocs.plugins." + __name__)

class ComputePods(BasePlugin) :

  def __init__(self):
    log.info("Initialized ComputePods plugin")

  def on_config(self, config) :
    if 'extra' not in config :
      config['extra'] = {}
    config['extra']['homepage'] = "/"
    return config

  def on_env(self, env, config, files) :
    env.globals['extracopyright'] = """&bull;
<a href="https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/" target="_blank">MkDocs Awesome Pages</a>
&bull;
<a href="https://mkdocstrings.github.io/" target="_blank">MkDocStrings</a>
&bull;
<a href="https://github.com/fralau/mkdocs-mermaid2-plugin" target="_blank">MkDocs Mermaid2</a>
&bull;
<a href="https://www.mkdocs.org" target="_blank">MkDocs</a>
"""
    return env
