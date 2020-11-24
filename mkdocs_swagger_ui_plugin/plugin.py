from mkdocs.plugins import BasePlugin
from pathlib import Path
import yaml
import os
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File
import mkdocs.utils
from jinja2 import Environment, PackageLoader
import json

mkdocs.utils.markdown_extensions = [
    '.markdown',
    '.mdown',
    '.mkdn',
    '.mkd',
    '.md',
    '.yml',
    '.yaml'
]

class MkDocsSwaggerUIPlugin(BasePlugin):
    TEMPLATE = Environment(loader=PackageLoader('mkdocs_swagger_ui_plugin', 'templates')).get_template('swagger_ui_template.j2')

    def on_nav(self, nav, config, files):
        for item in nav.items:
            if item.title == 'Reference':
                pages = []
                for link in item.children:

                    if (link.is_link):
                        file = File(link.url, config['docs_dir'], config['site_dir'], os.path.splitext(link.url)[0] + '/')
                        page = Page(link.title, file, config)
                        pages.append(page)
                    else:
                        pages.append(link)
                item.children = pages
        return nav

    def on_page_markdown(self, markdown, page, config, files):

        p = Path(page.file.abs_src_path)
        file = page.file
        if file.name != 'mkdocs' and (p.suffix == '.yml' or p.suffix == '.yaml'):
                yaml_dict = self.load_yaml(file)

                markdown = MkDocsSwaggerUIPlugin.TEMPLATE.render(content=json.dumps(yaml_dict))

        return markdown


    def load_yaml(self, file):
        with open(file.abs_src_path, 'r') as stream:
            try:
                content = yaml.load(stream, Loader=yaml.SafeLoader)
                return content
            except yaml.YAMLError as exc:
                print(exc)
