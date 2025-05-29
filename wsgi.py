#!/usr/bin/env python3
"""
WSGI entry point for Railway deployment.
"""

import os
import logging
from app import create_app

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # This runs when started directly (not via gunicorn)
    port = int(os.getenv("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=False)