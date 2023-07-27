# app/routes.py
from app.controllers.Super_Controller import handle_data
from flask import Blueprint, jsonify, request

routes_bp = Blueprint('routes', __name__)


def validate_data(data):
    # Add your data validation logic here.
    if 'basic-profile' not in data:
        return False
    return True


@routes_bp.route('/v1/entity/<string:uen>', methods=['POST'])
def process_data(uen):
    try:
        data = request.get_json()

        if not validate_data(data):
            return jsonify({'message': 'Invalid data format.'}), 400

        return handle_data(uen, data)

    except Exception as e:
        print("Error while processing the request:", str(e))
        return jsonify({'message': 'Error processing the request'}), 500
