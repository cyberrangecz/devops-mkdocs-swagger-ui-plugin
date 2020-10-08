from mkdocs.plugins import BasePlugin
from mkdocs_swagger_pages_plugin.swagger_yaml_to_html import render
from pathlib import Path
import yaml
import os
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File
import mkdocs.utils

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

    def on_nav(self, nav, config, files):
        for item in nav.items:
            if item.title == 'API':
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

                markdown = render(yaml_dict)
                # output_dir = os.path.realpath(os.path.join(
                #     config['site_dir'],
                #     os.path.splitext(file.src_path)[0])
                # )
                #
                # os.makedirs(output_dir)
                #
                # output_file = os.path.realpath(os.path.join(
                #     output_dir,
                #     'index.html')
                # )

        return markdown


    def load_yaml(self, file):
        with open(file.abs_src_path, 'r') as stream:
            try:
                content1 = yaml.load(stream, Loader=yaml.SafeLoader)
                return content1
            except yaml.YAMLError as exc:
                print(exc)
