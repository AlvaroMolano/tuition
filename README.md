## Tuition
A WIP tuition tool for online learning.


## App Structure
The application is created in a folder called tuition and has the following structure:

```
        .
        ├── MANIFEST.in
        ├── README.md
        ├── tuition
        │   ├── __init__.py
        │   ├── config
        │   │   ├── __init__.py
        │   │   └── desktop.py
        │   ├── hooks.py
        │   ├── tuition
        │   │   └── __init__.py
        │   ├── modules.txt
        │   ├── patches.txt
        │   └── templates
        │       ├── __init__.py
        │       ├── generators
        │       │   └── __init__.py
        │       ├── pages
        │       │   └── __init__.py
        │       └── statics
        ├── license.txt
        ├── requirements.txt
        └── setup.py
```



`config` folder contains application configuration info.

`desktop.py` is where desktop icons can be added to the Desk.

`hooks.py` is where integrations with the environment and other applications is mentioned.

`tuition` (inner) is a module that is bootstrapped. In Frappe, a module is where model and controller files reside.

`modules.txt` contains list of modules in the app. When you create a new module, it is required that you update it in this file.

`patches.txt` is where migration patches are written. They are python module references using the dot notation.

`templates` is the folder where web view templates are maintained. Templates for Login and other standard pages are bootstrapped in frappe.

`generators` are where templates for models are maintained, where each model instance has a separate web route, for example a Blog Post where each post has its unique web URL. In Frappe, the templating engine used is Jinja2.

`pages` is where single route templates are maintained. For example for a "/blog" type of page.

### Install
`bench --site library install-app https://github.com/AlvaroMolano/tuition.git`


### TODO
- Build questions & answers data structure and api.
- Build the create question-forms desk-tool.
- Build the questions-presenter view web page.


#### License

MIT