from flask import Flask, render_template

from app.webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)
    # Home route (no prefix)
    @app.route("/")
    def home():
        return "Welcome to Home "
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
