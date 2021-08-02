# mkdocs-computePods-plugin

A simple mkdocs plugin for use in the ComputePods documentation project.

This plugin is based upon the
[mkdocs-plugin-template](https://github.com/byrnereese/mkdocs-plugin-template)
contributed by [Byrne Reese](https://github.com/byrnereese) and is
modified using [its original MIT
license](https://github.com/byrnereese/mkdocs-plugin-template/blob/master/LICENSE).

At the moment we simply use the `on_template_context` to override the
`base_url` setting to match the base URL required by the ComputePods project.

## Installation

This mkdocs plugin has *not* (yet) been uploaded to
[pypi.org](https://pypi.org/).

So to install it you need to use:

```
pip install git+https://github.com/computePods/mkdocs-computePods-plugin/
```

([see Examples 5. Install a project from
VCS](https://pip.pypa.io/en/stable/cli/pip_install/#examples)) **or**

```
pipx install git+https://github.com/computePods/mkdocs-computePods-plugin/
```

([see installing from source
control](https://pypa.github.io/pipx/#installing-from-source-control)).

## Using the plugin

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - compute-pods
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll
> likely also want to add the `search` plugin. MkDocs enables it by
> default if there is no `plugins` entry set, but now you have to enable
> it explicitly.

More information about plugins in the [MkDocs
documentation](https://www.mkdocs.org/user-guide/).
