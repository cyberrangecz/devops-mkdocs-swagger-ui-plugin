# This repository is no longer active. The official Swagger plugin is now used.

## About
Plugin allows you to render `Swagger UI console` based on the swagger specification in YAML format. 

## Install
In plugin directory run command: 
```
 python3 setup.py install --prefix=$HOME/.local
``` 
to build package localy. Then in mkdocs repository run: 
```
pipenv install { path to the plugin repository }
pipenv sync
```
 
In `mkdocs.yaml` file add: 

```
plugins:
    - mkdocs-swagger-ui
```

and store YAML files in `/docs/reference/` directory. 

