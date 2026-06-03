{
    'name': 'Tablero OWL - Compras y Ventas',
    'version': '19.0.1.0.0',
    'summary': 'Dashboard de compras y ventas con OWL',
    'author': 'David Rodríguez',
    'category': 'Dashboard',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'views/dashboard_view.xml',
        'views/menu.xml'
    ],
   'assets': {
    'web.assets_backend': [
        'owl_tablero/static/src/dashboard.xml',
        'owl_tablero/static/src/dashboard.js',
        'owl_tablero/static/src/dashboard.css',
    ],
},
    'installable': True,
    'application': True,
}