from flask import Flask

from chess.game import Game
from routes.home import home_bp
from routes.api import api_bp, set_game


def create_app():
    app = Flask(__name__)

    game = Game()
    set_game(game)

    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
