# Fire Rescued

A sophisticated web application that helps predict and prevent burnout by analyzing your WHOOP health data combined with self-reported mood ratings. It leverages AI to provide personalized insights and recommendations based on your unique health patterns.

## Features

- **WHOOP API Integration:** Automatically fetches daily health metrics (recovery score, strain, HRV, sleep quality)
- **Mood Tracking:** Simple and intuitive interface to log daily mood and notes
- **Advanced Analytics:** Sophisticated burnout risk algorithm using multiple health metrics
- **Data Visualization:** Interactive charts showing trends and correlations over time
- **AI-Powered Insights:** Personalized recommendations and analysis using OpenAI
- **Modern Dashboard:** Clean, visually appealing interface optimized for usability
- **Multi-device Support:** Responsive design works on desktop and mobile
- **Cloud Synchronization:** Secure data storage with Supabase (with SQLite fallback)

## Technology Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Database:** Supabase (PostgreSQL) with SQLite fallback
- **API:** RESTful architecture with JSON endpoints
- **Authentication:** Secure user login via Supabase Auth
- **Data Analysis:** Pandas, NumPy, SciPy
- **Visualization:** Plotly interactive charts
- **AI/ML:** OpenAI API integration
- **Frontend:** HTML, CSS, JavaScript with Bootstrap 5

## Installation

### Prerequisites

- Python 3.8 or higher
- WHOOP account and API credentials
- Supabase account (recommended)
- OpenAI API key (for AI insights)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/burnout-predictor.git
   cd burnout-predictor
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp example.env .env
   # Edit .env file with your credentials
   ```

4. **Initialize the database**
   ```bash
   # If using Supabase (recommended)
   python -m app.database.supabase
   
   # Or create a test account with sample data
   python create_test_account.py
   ```

### Running the Application

**Development mode**
```bash
python run.py
```

**Production mode**
```bash
gunicorn 'app:create_app()' --bind 0.0.0.0:$PORT
```

Access the application at http://localhost:3000

## Project Structure

```
burnout-predictor/
├── app/                  # Application package
│   ├── __init__.py       # App factory and configuration
│   ├── auth/             # Authentication
│   ├── api/              # API endpoints
│   ├── core/             # Main functionality
│   ├── database/         # Database access
│   ├── services/         # Business logic
│   ├── static/           # Assets (CSS, JS, images)
│   ├── templates/        # HTML templates
│   └── utils/            # Common utilities
├── tests/                # Test suite
├── .env                  # Environment variables (create from example.env)
├── example.env           # Example environment file
├── requirements.txt      # Python dependencies
├── run.py                # Application entry point
└── README.md             # Documentation
```

## WHOOP API Setup

1. Create a developer account at [WHOOP Developer Portal](https://developer.whoop.com/)
2. Register a new application
3. Set your redirect URI to `http://localhost:3000/` (development) or your production URL
4. Add your client ID and secret to the `.env` file

## Supabase Setup

Refer to [SUPABASE_SETUP.md](SUPABASE_SETUP.md) for detailed instructions on setting up your Supabase project.

## OpenAI Setup

1. Create an account at [OpenAI](https://platform.openai.com/)
2. Generate an API key
3. Add the key to your `.env` file as `OPENAI_API_KEY`

## Usage Guide

1. **Account Setup**
   - Sign up for an account
   - Connect your WHOOP account via OAuth

2. **Daily Usage**
   - View your health metrics dashboard
   - Log your daily mood (1-10 scale)
   - Check your burnout risk score

3. **Analysis**
   - Explore trend charts
   - View correlations between metrics
   - Get AI-powered insights and recommendations

4. **Settings**
   - Configure integrations
   - Manage notification preferences
   - Update AI model settings

## Data Privacy & Security

- All data is encrypted in transit and at rest
- Supabase provides enterprise-grade security for cloud storage
- Local SQLite option available for complete privacy
- OpenAI API calls follow strict data minimization principles
- No third-party analytics or tracking

## Deploying to Production

### 🚂 Railway (Recommended)

**Railway is the perfect platform for Fire Rescued** because it natively supports Python Flask applications with all features intact.

✅ **What works perfectly on Railway:**
- Full Flask application with all routes
- Background APScheduler for WHOOP data fetching
- Database connections to Supabase
- Environment variables and secrets management
- Real-time logging and monitoring
- Automatic deployments from GitHub

**Quick Deploy:**
1. Sign up at [Railway](https://railway.app)
2. Connect your GitHub repository
3. Configure environment variables
4. Deploy automatically!

📖 **[Complete Railway Deployment Guide](docs/RAILWAY_DEPLOYMENT.md)**

### Alternative: Vercel (Advanced Users)

Due to Vercel's serverless function size limitations with Python projects, there are two deployment approaches:

### Option 1: Simple Landing Page Deployment

This approach deploys a simple landing page as a placeholder for your full application:

1. **Navigate to the minimal deployment directory**
   ```bash
   cd vercel-deploy
   ```

2. **Install Vercel CLI and login**
   ```bash
   npm install -g vercel
   vercel login
   ```

3. **Deploy the landing page**
   ```bash
   vercel --prod
   ```

The result will be a simple landing page that serves as a placeholder for your full application. You can view the deployed site at: https://vercel-deploy-ksuk0zgjy-wesley-wesleydaltons-projects.vercel.app

### Option 2: Full Application Deployment (Advanced)

For the full application to work on Vercel, you would need to:

1. **Split your application into smaller functions**
   - Restructure the app into API routes
   - Use frontend-only components where possible

2. **Use Vercel edge functions or middleware**
   - Convert Flask routes to serverless functions
   - Optimize package sizes

3. **Set up environment variables in the Vercel dashboard**
   - Go to your project settings in the Vercel dashboard
   - Navigate to the "Environment Variables" section
   - Add all the required variables from your .env file

### Recommended Alternative

For a Python application of this complexity, consider alternatives like:
- Heroku
- Railway
- DigitalOcean App Platform
- Google Cloud Run
- AWS Elastic Beanstalk

These platforms better support full Flask applications with their dependencies.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- WHOOP for providing the health metrics API
- Supabase for the excellent database platform
- OpenAI for the AI insights technology
- All contributors who have helped build this application