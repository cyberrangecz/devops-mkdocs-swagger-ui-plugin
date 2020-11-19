from setuptools import setup, find_packages


setup(
    name='mkdocs-swagger-pages-plugin',
    version='1.0.0',
    description='A MkDocs plugin to render yaml files as swagger UI.',
    long_description=read('README.md'),
    keywords='mkdocs swagger yaml',
    author='KYPO Team',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
        'PyYAML>=5.1'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-swagger-ui = mkdocs_swagger_pages_plugin.plugin:MkDocsSwaggerPlugin'
        ]
    }
)
