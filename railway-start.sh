#!/bin/bash

# Railway startup script for Fire Rescued
echo "🚂 Starting Fire Rescued on Railway..."

# Set production environment
export FLASK_ENV=production

# Initialize database if needed
echo "📊 Checking database connection..."
python -c "
try:
    from app.database import init_database
    from app import create_app
    app = create_app()
    with app.app_context():
        init_database(app)
    print('✅ Database connection successful')
except Exception as e:
    print(f'⚠️  Database initialization note: {e}')
"

# Start the application
echo "🔥 Launching Fire Rescued application..."
exec gunicorn 'wsgi:app' --bind 0.0.0.0:$PORT --log-level info --workers 1 --timeout 120 