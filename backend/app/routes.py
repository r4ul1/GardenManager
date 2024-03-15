from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/health')
def health():
    return "The GartenManager is healthy!"
