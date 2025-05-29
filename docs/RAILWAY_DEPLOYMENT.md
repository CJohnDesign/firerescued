# 🚂 Railway Deployment Guide for Fire Rescued

This guide will walk you through deploying Fire Rescued to [Railway](https://railway.app), a platform designed for full-stack applications.

## 🎯 Why Railway?

Railway is the perfect deployment platform for Fire Rescued because:
- ✅ **Native Python/Flask support** - No serverless conversion needed
- ✅ **Background schedulers work** - Your APScheduler for WHOOP data fetching will run perfectly
- ✅ **Built-in PostgreSQL** - Seamless Supabase integration
- ✅ **Simple environment variables** - Easy configuration management
- ✅ **Automatic deployments** - Deploy from GitHub automatically
- ✅ **Real logs and monitoring** - Better debugging than serverless platforms

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository

Your repository is already Railway-ready! We've created:
- `railway.json` - Railway configuration
- `requirements-railway.txt` - Optimized dependencies
- `railway-start.sh` - Startup script
- Updated `wsgi.py` - Production WSGI entry point

### Step 2: Create Railway Account & Project

1. **Sign up at [Railway](https://railway.app)**
   - Use your GitHub account for easier deployment

2. **Create a new project**
   ```bash
   # Install Railway CLI (optional but recommended)
   npm install -g @railway/cli
   railway login
   ```

3. **Connect your repository**
   - Go to Railway dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `firerescued` repository

### Step 3: Configure Environment Variables

In your Railway project dashboard, add these environment variables:

#### Required Variables
```bash
# Flask Configuration
FLASK_ENV=production
FLASK_SECRET_KEY=your-secret-key-here
PORT=3000

# WHOOP API (get from https://developer.whoop.com/)
WHOOP_CLIENT_ID=your-whoop-client-id
WHOOP_CLIENT_SECRET=your-whoop-client-secret
REDIRECT_URI=https://your-railway-domain.railway.app

# Supabase Database (get from https://supabase.com)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-key
SUPABASE_USER_ID=your-user-id

# OpenAI (get from https://platform.openai.com/)
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-4o
```

#### Optional Variables
```bash
# Monitoring (if you want detailed logging)
NEW_RELIC_LICENSE_KEY=your-license-key
```

### Step 4: Deploy!

Railway will automatically deploy when you push to your main branch. You can also trigger deployments manually:

```bash
# Using Railway CLI
railway up

# Or trigger from GitHub by pushing changes
git add .
git commit -m "Deploy to Railway"
git push origin main
```

### Step 5: Configure Domain (Optional)

1. In your Railway dashboard, go to Settings
2. Click "Domains"
3. Add a custom domain or use the provided Railway subdomain

## 🔧 Post-Deployment Configuration

### Database Setup
Your Supabase database should work automatically, but you can verify:

1. Check Railway logs for database connection messages
2. Visit your app URL and ensure no database errors
3. Test user registration/login functionality

### WHOOP Integration Testing
1. Navigate to `/auth` on your deployed app
2. Test the WHOOP OAuth flow
3. Verify data fetching works

### Monitoring & Logs
- View real-time logs in Railway dashboard
- Set up alerts for errors
- Monitor resource usage

## 🔥 Advanced Railway Features

### Automatic Deployments
Railway will automatically deploy when you push to main branch. To disable:
```bash
railway settings --auto-deploy false
```

### Custom Build Command
If you need custom build steps, update `railway.json`:
```json
{
  "build": {
    "builder": "NIXPACKS",
    "buildCommand": "pip install -r requirements-railway.txt && python -m app.database.supabase"
  }
}
```

### Scaling
Railway automatically handles scaling, but you can configure:
- Memory limits
- CPU allocation
- Auto-scaling rules

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Verify Supabase environment variables
   - Check if Supabase project is active
   - Ensure Railway has internet access to Supabase

2. **WHOOP API Issues**
   - Update redirect URI in WHOOP developer console
   - Verify client ID/secret are correct
   - Check OAuth callback URL

3. **Build Failures**
   - Check Railway build logs
   - Verify all dependencies in requirements-railway.txt
   - Ensure Python version compatibility

4. **Application Won't Start**
   - Check Railway application logs
   - Verify PORT environment variable
   - Ensure wsgi.py is properly configured

### Debugging Commands
```bash
# View logs
railway logs

# Connect to your deployed app
railway shell

# Check environment variables
railway variables
```

## 💰 Cost Estimate

Railway pricing (as of 2024):
- **Hobby Plan**: $5/month - Perfect for development and small usage
- **Pro Plan**: $20/month - Production ready with more resources
- **Team Plan**: $50/month - For teams with collaboration features

Your Fire Rescued app should run comfortably on the Hobby plan initially.

## ✅ Production Checklist

Before going live:
- [ ] All environment variables configured
- [ ] Custom domain set up (optional)
- [ ] Database backups enabled in Supabase
- [ ] Error monitoring configured
- [ ] WHOOP OAuth tested end-to-end
- [ ] User registration/login tested
- [ ] Data fetching scheduled job tested
- [ ] Performance tested with sample data

## 🔗 Useful Links

- [Railway Documentation](https://docs.railway.app/)
- [Railway CLI](https://docs.railway.app/develop/cli)
- [Railway Templates](https://railway.app/templates)
- [Python on Railway](https://docs.railway.app/guides/python)

---

## 🎉 Next Steps

Once deployed, your Fire Rescued application will be available at your Railway URL. Users can:
1. Register accounts
2. Connect their WHOOP devices
3. Track daily mood ratings
4. View burnout risk analysis
5. Get AI-powered health insights

Happy deploying! 🚀 