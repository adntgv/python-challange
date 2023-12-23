from flask import Blueprint, request, jsonify
from ..database.models import Image
from app.services.color_mapper import apply_color_map

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/images', methods=['GET'])
def get_images():
    depth_min = request.args.get('depth_min', type=float)
    depth_max = request.args.get('depth_max', type=float)

    if depth_min is None or depth_max is None:
        return jsonify({'error': 'Depth range parameters are required'}), 400

    images = Image.query.filter(Image.depth.between(depth_min, depth_max)).all()
    if not images:
        return jsonify({'message': 'No images found in the specified depth range'}), 404

    return jsonify([{'depth': img.depth, 'image': apply_color_map(img.image_data).tolist()} for img in images])
