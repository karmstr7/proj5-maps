"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
# app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


#############

# app.debug = CONFIG.DEBUG
# if app.debug:
#     app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    # print("Opening for global access on port {}".format(CONFIG.PORT))
    # app.run(port=CONFIG.PORT, host="0.0.0.0")
    app.debug = True
    app.run()
