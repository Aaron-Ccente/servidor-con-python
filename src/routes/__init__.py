from flask import Blueprint

# Define a blueprint for the routes
api_bp = Blueprint('api', __name__)

# Import routes here
from . import example_routes  # Replace with actual route files as needed

# Register the blueprint in the main application file (main.py)