## About
Plugin allows you to render `Swagger UI console` based on the swagger specification in YAML format. 

## Install
In plugin directory run command: 
```
 python setup.py install --prefix=$HOME/.local
``` 
to build package localy. Then in mkdocs repository run: 
```
pipenv install /home/dominik/Desktop/Utilities/mkdocs-swagger-pages-plugin/
pipenv sync
```
 
In `mkdocs.yaml` file add: 

```
plugins:
    - mkdocs-swagger-ui
```

and store YAML files in `/docs/api/` directory. 

