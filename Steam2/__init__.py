from flask import Flask
from flask_moment import Moment


__version__ = "0.1.0"

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

moment = Moment(app)

import Steam2.routes  # noqa: E402, F401
