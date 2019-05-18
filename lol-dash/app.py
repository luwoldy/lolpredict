import dash

external_stylesheets = ['https://necolas.github.io/normalize.css/8.0.1/normalize.css',"https://fonts.googleapis.com/icon?family=Material+Icons","https://unpkg.com/purecss@1.0.0/build/pure-min.css"]
external_scripts = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,external_scripts=external_scripts)
server = app.server
app.config.suppress_callback_exceptions = True

