from flask import Flask
from api.main.views import main_blueprint
from api.search.views import search_blueprint
from api.loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(loader_blueprint)

app.run()
