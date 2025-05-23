# Architecture Overview
## Fire Rescued System Architecture

**Version**: 1.0  
**Last Updated**: {{ now.strftime('%B %d, %Y') }}  
**Architecture Team**: Fire Rescued Engineering  

---

## 🏗️ System Overview

Fire Rescued is a Flask-based web application that integrates WHOOP health data with user-reported mood tracking to predict and prevent burnout. The system follows a modular, scalable architecture with clear separation of concerns.

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │    │  Mobile Device  │    │  API Clients    │
│   (Desktop)     │    │   (Responsive)  │    │  (Future)       │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────┴─────────────┐
                    │     Load Balancer        │
                    │    (Future/Scaling)      │
                    └─────────────┬─────────────┘
                                  │
              ┌───────────────────┴───────────────────┐
              │            Flask Application          │
              │         (Python 3.8+)               │
              └───┬───────────────────────────────┬───┘
                  │                               │
    ┌─────────────┴─────────────┐    ┌──────────┴──────────┐
    │      External APIs        │    │    Data Storage     │
    │                          │    │                     │
    │  ┌─────────────────────┐  │    │  ┌───────────────┐  │
    │  │    WHOOP API        │  │    │  │   Supabase    │  │
    │  │   (Health Data)     │  │    │  │ (PostgreSQL)  │  │
    │  └─────────────────────┘  │    │  └───────────────┘  │
    │                          │    │                     │
    │  ┌─────────────────────┐  │    │  ┌───────────────┐  │
    │  │   OpenAI API        │  │    │  │    SQLite     │  │
    │  │  (AI Insights)      │  │    │  │  (Fallback)   │  │
    │  └─────────────────────┘  │    │  └───────────────┘  │
    └─────────────────────────────┘    └─────────────────────┘
```

## 🧩 Core Components

### 1. **Flask Application Layer**
- **Framework**: Flask 2.x with Python 3.8+
- **Architecture**: Blueprint-based modular design
- **Session Management**: Flask-Session with filesystem storage
- **Template Engine**: Jinja2 for server-side rendering

### 2. **Data Layer**
- **Primary Database**: Supabase (PostgreSQL) for production
- **Fallback Database**: SQLite for development and offline capability
- **ORM**: Direct SQL queries with database abstraction layer
- **Caching**: In-memory caching for frequently accessed data

### 3. **External Integrations**
- **WHOOP API**: OAuth 2.0 integration for health data
- **OpenAI API**: GPT-4 integration for AI insights
- **Supabase Auth**: User authentication and authorization

### 4. **Background Services**
- **Data Sync**: APScheduler for automated WHOOP data fetching
- **Health Calculations**: Burnout risk scoring algorithms
- **Analytics**: Statistical analysis and correlation computation

## 📁 Directory Structure

```
fire-rescued/
├── app/                      # Main application package
│   ├── __init__.py          # App factory and configuration
│   ├── auth/                # Authentication module
│   │   ├── __init__.py     # Blueprint registration
│   │   ├── routes.py       # Auth routes (login, signup, logout)
│   │   └── utils.py        # Auth utilities and decorators
│   ├── core/               # Core application functionality
│   │   ├── __init__.py     # Blueprint registration
│   │   └── routes.py       # Main app routes (dashboard, settings)
│   ├── api/                # REST API endpoints
│   │   ├── __init__.py     # API blueprint
│   │   └── routes.py       # API route handlers
│   ├── database/           # Database abstraction layer
│   │   ├── __init__.py     # Database configuration
│   │   ├── supabase.py     # Supabase operations
│   │   └── sqlite.py       # SQLite fallback operations
│   ├── services/           # Business logic layer
│   │   ├── whoop_service.py    # WHOOP API integration
│   │   ├── ai_service.py       # OpenAI integration
│   │   └── analysis_service.py # Health data analysis
│   ├── utils/              # Common utilities
│   ├── templates/          # Jinja2 HTML templates
│   └── static/            # CSS, JS, and static assets
├── docs/                  # Documentation
├── tests/                 # Test suite
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
└── run.py               # Application entry point
```

## 🔄 Data Flow Architecture

### 1. **User Authentication Flow**
```
User → Login Form → Flask Auth → Supabase Auth → Session Storage → Dashboard
```

### 2. **WHOOP Data Integration Flow**
```
WHOOP API → OAuth Flow → Token Storage → Scheduled Fetch → Data Processing → Database Storage
```

### 3. **Mood Tracking Flow**
```
User Input → Form Validation → Mood Processing → Database Storage → Analytics Update
```

### 4. **AI Insights Flow**
```
User Query → Context Preparation → OpenAI API → Response Processing → Chat Interface
```

### 5. **Burnout Risk Calculation Flow**
```
Health Data + Mood Data → Risk Algorithm → Score Calculation → Trend Analysis → Dashboard Display
```

## 🛡️ Security Architecture

### Authentication & Authorization
- **User Auth**: Supabase Auth with JWT tokens
- **Session Management**: Server-side session storage
- **API Access**: OAuth 2.0 for external service integration
- **Route Protection**: Decorator-based access control

### Data Security
- **Encryption**: All data encrypted in transit (HTTPS) and at rest
- **API Keys**: Environment-based configuration management
- **Database**: Row-level security policies in Supabase
- **Backup**: Automated daily backups with encryption

### Privacy Protection
- **Data Minimization**: Collect only necessary health metrics
- **User Control**: Granular privacy settings and data deletion
- **Anonymization**: Personal data anonymized for analytics
- **Compliance**: HIPAA-aware data handling procedures

## ⚡ Performance Architecture

### Caching Strategy
- **Template Caching**: Jinja2 template compilation caching
- **Data Caching**: In-memory caching for dashboard metrics
- **Static Assets**: CDN delivery for CSS/JS (future enhancement)
- **Database**: Query optimization and connection pooling

### Optimization Techniques
- **Lazy Loading**: Charts and heavy content load on demand
- **Code Splitting**: Modular JavaScript loading
- **Image Optimization**: Compressed and responsive images
- **Gzip Compression**: Server-side response compression

### Monitoring & Observability
- **Logging**: Structured logging with different levels
- **Error Tracking**: Exception handling and reporting
- **Performance Metrics**: Response time and resource usage monitoring
- **Health Checks**: System status and dependency monitoring

## 🔌 Integration Architecture

### WHOOP API Integration
```python
# OAuth 2.0 Flow Implementation
class WhoopService:
    def authenticate_user(self, auth_code):
        # Exchange auth code for access token
        
    def fetch_daily_metrics(self, user_id):
        # Retrieve health data with error handling
        
    def sync_historical_data(self, user_id, days=30):
        # Batch fetch historical data
```

### OpenAI Integration
```python
# AI Service Implementation
class AIService:
    def generate_insights(self, user_data, query):
        # Process user context and generate response
        
    def analyze_patterns(self, health_metrics):
        # Pattern recognition and recommendations
```

### Database Abstraction
```python
# Dual Database Support
if USE_SUPABASE:
    from app.database.supabase import get_daily_metrics
else:
    from app.database.sqlite import get_metrics_by_date
```

## 📊 Data Architecture

### Data Models

#### User Model
- **Fields**: ID, email, created_at, preferences
- **Relations**: One-to-many with health records
- **Storage**: Supabase Auth + custom user_profiles table

#### Health Metrics Model
- **Fields**: user_id, date, recovery_score, strain, sleep_quality, hrv
- **Source**: WHOOP API
- **Storage**: daily_metrics table with date partitioning

#### Mood Tracking Model
- **Fields**: user_id, date, mood_rating, notes, context
- **Source**: User input
- **Storage**: Embedded in daily_metrics table

#### Burnout Risk Model
- **Fields**: user_id, date, risk_score, factors, recommendations
- **Source**: Algorithm calculation
- **Storage**: Calculated field with historical tracking

### Data Relationships
```sql
users (1) ←→ (many) daily_metrics
users (1) ←→ (many) whoop_tokens
users (1) ←→ (many) ai_interactions
```

## 🚀 Deployment Architecture

### Current Deployment (Development)
- **Local Development**: Flask development server
- **Database**: Supabase cloud instance
- **Environment**: Python virtual environment
- **Configuration**: Environment variables via .env

### Production Deployment (Planned)
- **Application Server**: Gunicorn with multiple workers
- **Reverse Proxy**: Nginx for static file serving and SSL
- **Database**: Supabase with connection pooling
- **Monitoring**: Logging and error tracking integration

### Cloud Infrastructure (Future)
- **Platform**: Railway, Heroku, or DigitalOcean App Platform
- **CDN**: CloudFlare for static asset delivery
- **Monitoring**: Application performance monitoring
- **Scaling**: Horizontal scaling with load balancer

## 🔮 Future Architecture Considerations

### Scalability Enhancements
- **Microservices**: Split analytics and AI services
- **API Gateway**: Centralized API management and rate limiting
- **Caching Layer**: Redis for distributed caching
- **Queue System**: Background job processing with Celery

### Advanced Features
- **Real-time Updates**: WebSocket connections for live data
- **Machine Learning**: Custom ML models for pattern recognition
- **Multi-tenant**: Organization-level data isolation
- **Mobile Apps**: Native mobile applications with shared API

### Technology Evolution
- **Frontend Framework**: Consider React or Vue.js for enhanced UX
- **Database**: Evaluate time-series databases for health data
- **AI/ML**: Custom machine learning pipeline for predictions
- **Analytics**: Business intelligence and reporting platform

## 🧪 Testing Architecture

### Test Strategy
- **Unit Tests**: Individual component testing
- **Integration Tests**: Database and API integration testing
- **End-to-End Tests**: Complete user workflow testing
- **Performance Tests**: Load testing and benchmarking

### Test Environment
- **Database**: Separate test database instances
- **Mocking**: External API mocking for reliable tests
- **CI/CD**: Automated testing pipeline
- **Coverage**: Code coverage tracking and reporting

---

## 📚 Related Documentation

- [**Frontend Architecture**](./frontend.md) - Client-side architecture details
- [**Backend Architecture**](./backend.md) - Server-side implementation details
- [**Database Design**](./database.md) - Data models and schema design
- [**API Documentation**](../api/README.md) - REST API specifications
- [**Security Guide**](../security/README.md) - Security implementation details

---

**Maintained by**: Fire Rescued Architecture Team  
**Review Schedule**: Quarterly architecture reviews  
**Next Review**: Q2 2024 