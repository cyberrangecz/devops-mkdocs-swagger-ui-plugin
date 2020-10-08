from setuptools import setup, find_packages


setup(
    name='mkdocs-swagger-pages-plugin',
    version='1.0.0',
    description='A MkDocs plugin to render yaml files as swagger UI.',
    long_description='',
    keywords='mkdocs swagger yaml',
    author='Dominik Pilar',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-swagger-ui = mkdocs_swagger_pages_plugin.plugin:MkDocsSwaggerPlugin'
        ]
    }
)
