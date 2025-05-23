"""
API blueprint for Fire Rescued
Provides JSON API endpoints for frontend integration
"""

from flask import Blueprint

api_bp = Blueprint('api', __name__)

# Import routes to register them with the blueprint
from . import routes