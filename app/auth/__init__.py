"""
Authentication system for Fire Rescued
Handles user signup, login, and session management.
"""

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

# Import routes to register them with the blueprint
from . import routes