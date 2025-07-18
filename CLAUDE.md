# Fire Rescued

The Fire Rescued is a web application that helps predict and prevent burnout by analyzing WHOOP health data. It leverages AI to provide personalized insights and recommendations based on health patterns.

## Key Features

- **WHOOP Integration:** Seamless data sync with WHOOP wearables
- **AI Insights:** Powered by OpenAI for personalized recommendations  
- **Burnout Risk Algorithm:** Sophisticated algorithm using multiple health metrics
- **Visual Analytics:** Interactive charts and trend analysis
- **Daily Tracking:** Easy mood input and metric tracking

## Project Structure

```
/Users/wesdalton/Desktop/Burnout/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── auth/                    # Authentication routes
│   ├── core/                    # Main application routes
│   ├── database/                # Database models and operations
│   ├── prompts/                 # AI system prompts
│   ├── services/                # Business logic services
│   ├── static/                  # CSS, JS, images
│   ├── templates/               # Jinja2 HTML templates
│   └── utils/                   # Utility functions
├── docs/                        # Project documentation
├── venv/                        # Virtual environment
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
└── run.py                       # Application entry point
```

## Database Schema

### Metrics Table
- user_id (Foreign Key)
- date (Date)
- recovery_score (Integer 0-100)
- hrv (Float - Heart Rate Variability)
- resting_hr (Float - Resting Heart Rate)
- strain (Float 0-21)
- sleep_quality (Float 0-100)
- burnout_current (calculated risk score 0-100)

### Burnout Risk Calculation
The burnout risk algorithm uses multiple factors:
- **Recovery Score (40%):** WHOOP recovery percentage
- **Sleep Quality (30%):** Sleep efficiency and duration
- **HRV Analysis (15%):** Heart rate variability trends  
- **Strain Balance (15%):** Strain-to-recovery ratio

## Current Features

1. WHOOP data integration and sync
2. Daily mood tracking interface
3. Burnout risk gauge with actionable recommendations
4. Time series visualization of health metrics
5. AI-powered insights and recommendations
6. Multi-day trend analysis
7. Responsive design with modern UI

## Recent Updates

- Added comprehensive AI insights system with OpenAI integration
- Enhanced dashboard with Apple-inspired design elements
- Implemented sophisticated burnout risk calculation model
- Added time series plots with multiple health metrics
- Improved mobile responsiveness and accessibility
- Implemented a more visually appealing burnout risk display
- Added correlation analysis between different health metrics

## Key Templates
- **dashboard.html** - Main user interface with health metrics visualization
- **input.html** - Interface for logging daily mood ratings
- **ai_insights.html** - Detailed AI insights page
- **layout.html** - Base template with common elements

## Design Elements
The app follows an Apple-inspired design language with:
- Clean, minimalist card-based interface
- Meaningful insights cards with color-coding (positive, neutral, negative)
- Simplified data visualizations focusing on trends and actionable insights
- Consistent spacing, typography, and visual hierarchy
- Interactive elements with subtle animations

## Common Tasks

### Running the App
```bash
python3 run.py  # Starts development server on http://127.0.0.1:3000
```

### Data Model
Key data entities:
1. **User** - Authenticated user with email/password
2. **DailyMetrics** - Health data for a specific date:
   - recovery_score (0-100)
   - hrv (heart rate variability in ms)
   - resting_hr (beats per minute)
   - strain (0-21 scale) 
   - sleep_quality (0-100)
   - mood_rating (1-10, user-input)
   - notes (text, user-input)
   - burnout_current (calculated risk score 0-100)

### Burnout Risk Calculation
The burnout risk algorithm uses multiple factors:
- Recovery scores (25% weight)
- Mood ratings (30% weight)
- HRV metrics (15% weight)
- Sleep quality (15% weight)
- Strain-recovery balance (15% weight)

### Dashboard Visualization
The dashboard has been redesigned to focus on:
1. Key metrics with trend indicators
2. Simplified, Apple-like charts for health data
3. Burnout risk gauge with actionable recommendations
4. AI-powered insights section
5. Recent history timeline

## Design Philosophy
The application has been specifically redesigned to follow Apple's design principles:
- Focus on clarity and simplicity
- Content-focused design with plenty of white space
- Visual hierarchy that guides users to important information
- Action-oriented recommendations rather than just data visualization
- Accessibility through clear typography and color-coding

## Recent Changes
- Completely redesigned the metrics visualization to be more consumer-friendly
- Added Apple-inspired insight cards to replace complex graphs
- Implemented a more visually appealing burnout risk display
- Enhanced the AI insights section with better styling and clearer information
- Simplified technical visualizations to provide actionable insights

## Common Issues
- Some Jinja2 template expressions may need careful handling of None values
- WHOOP API integration requires OAuth authentication
- Supabase tables sometimes show initialization errors but app functions normally

## Accessibility Considerations
- Color-coding is supplemented with clear text labels
- Status indicators use both icons and text
- Numeric values have clear context and explanations