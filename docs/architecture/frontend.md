# Frontend Architecture

## 🏗️ Framework & Technology Stack

### Core Framework
- **Flask** with **Jinja2 Templating Engine**
- **Server-Side Rendering (SSR)** approach
- **Bootstrap 5** for responsive UI framework
- **Custom CSS** with CSS Variables for design system
- **Vanilla JavaScript** for interactive functionality

### Key Libraries & Dependencies
```html
<!-- Core Frameworks -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

<!-- Icons & Typography -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<!-- Data Visualization -->
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```

## 📁 File Structure

```
app/
├── templates/           # Jinja2 HTML templates
│   ├── layout.html     # Base template with navigation
│   ├── dashboard.html  # Main dashboard interface
│   ├── ai_insights.html # AI chat interface
│   ├── input.html      # Mood input form
│   ├── settings.html   # User settings
│   ├── login.html      # Authentication
│   └── signup.html     # User registration
└── static/
    └── css/
        └── style.css   # Custom styles and design system
```

## 🎨 Design System

### CSS Variables (Design Tokens)
```css
:root {
    /* Color Palette */
    --primary-color: #4361ee;      /* Main brand color */
    --secondary-color: #7209b7;    /* Secondary accent */
    --success-color: #38b000;      /* Positive indicators */
    --warning-color: #f9c74f;      /* Caution indicators */
    --danger-color: #ef476f;       /* Negative/high risk */
    --neutral-color: #adb5bd;      /* Neutral elements */
    --dark-color: #2b2d42;         /* Dark text/borders */
    --light-color: #f8f9fa;        /* Light backgrounds */
    
    /* Design System */
    --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    --border-radius: 10px;
    --transition-speed: 0.3s;
}
```

### Typography System
- **Primary Font**: Inter (with fallbacks)
- **Font Stack**: `'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto`
- **Hierarchy**: H1-H6 with consistent weights (600 for headings)
- **Line Height**: 1.5 for optimal readability

### Component Architecture

#### 1. **Layout System**
- **Base Template**: `layout.html` provides consistent navigation and structure
- **Block System**: Jinja2 blocks for `content` and `scripts`
- **Responsive Grid**: Bootstrap's 12-column grid system
- **Navigation**: Sticky top navigation with user dropdown

#### 2. **Card Components**
```css
.metric-card {
    border-radius: var(--border-radius);
    box-shadow: var(--card-shadow);
    transition: transform var(--transition-speed);
}

.primary-metric {
    background-color: #fff;
    padding: 1.5rem;
    position: relative;
}
```

#### 3. **Interactive Elements**
- **Buttons**: Consistent sizing and hover states
- **Forms**: Bootstrap form components with custom styling
- **Charts**: Plotly.js integration for data visualization
- **Modals**: Bootstrap modals for secondary actions

## 🔄 State Management

### Client-Side State
- **Local Storage**: User preferences and temporary data
- **Session Storage**: Current session data
- **URL Parameters**: Date selection and navigation state
- **Form State**: Managed through standard HTML forms

### Server-Side State
- **Flask Sessions**: User authentication and session data
- **Database**: Persistent application state
- **Context Variables**: Template data passed from Flask routes

## 📱 Responsive Design

### Breakpoint Strategy
```css
/* Mobile First Approach */
@media (max-width: 768px) {
    .metrics-grid {
        grid-template-columns: 1fr;  /* Stack on mobile */
    }
    
    .metrics-secondary {
        flex-direction: column;      /* Vertical layout */
    }
}
```

### Key Responsive Features
- **Flexible Grid**: CSS Grid with responsive columns
- **Adaptive Navigation**: Collapsible mobile menu
- **Touch-Friendly**: Appropriate tap targets (44px minimum)
- **Viewport Optimization**: Proper meta viewport configuration

## 🎯 User Experience Patterns

### Navigation Patterns
1. **Primary Navigation**: Top-level features (Dashboard, AI Insights)
2. **Date Navigation**: Custom calendar widget with risk visualization
3. **Contextual Actions**: Inline edit/add buttons
4. **Breadcrumbs**: Clear navigation hierarchy

### Interaction Patterns
1. **Progressive Disclosure**: Show more details on demand
2. **Inline Editing**: Edit mood ratings without page reload
3. **Real-time Feedback**: Loading states and success messages
4. **Keyboard Navigation**: Accessible keyboard interactions

### Data Visualization
- **Health Metrics**: Large, easy-to-read primary metrics
- **Trend Charts**: Interactive Plotly charts with hover details
- **Status Indicators**: Color-coded health status pills
- **Calendar Heatmap**: Risk visualization over time

## 🔧 Performance Optimizations

### Loading Strategy
- **Critical CSS**: Inline critical styles for above-the-fold content
- **Progressive Enhancement**: Works without JavaScript
- **Lazy Loading**: Charts and heavy content load on demand
- **CDN Resources**: External libraries from CDN

### Caching Strategy
- **Static Assets**: Long-term caching for CSS/JS
- **Template Caching**: Flask template caching for performance
- **Browser Caching**: Appropriate cache headers

## 🚀 Interactive Features

### AJAX Functionality
```javascript
// Example: AI Insights Chat
fetch('/ai-insights', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `query=${encodeURIComponent(query)}`
})
.then(response => response.text())
.then(html => {
    // Update chat interface
});
```

### Dynamic Content Updates
- **Chart Refreshing**: Update visualizations without page reload
- **Form Submissions**: AJAX form handling for smooth UX
- **Real-time Data**: Live updates for AI insights
- **Calendar Navigation**: Dynamic date selection

## 🎨 Visual Design Principles

### Color Strategy
- **Semantic Colors**: Colors convey meaning (green = good, red = risk)
- **Accessibility**: WCAG 2.1 AA contrast compliance
- **Consistency**: Unified color palette across all components
- **Health-Focused**: Colors chosen for health/wellness context

### Visual Hierarchy
1. **Primary Metrics**: Large, prominent display
2. **Secondary Data**: Smaller, supporting information
3. **Actions**: Clear, discoverable buttons
4. **Navigation**: Subtle but accessible

### Animation & Transitions
- **Subtle Animations**: 0.3s transitions for smooth interactions
- **Hover Effects**: Card lift effects and button state changes
- **Loading States**: Spinners and progress indicators
- **Page Transitions**: Smooth navigation between sections

## 🔍 Accessibility Features

### WCAG Compliance
- **Semantic HTML**: Proper heading hierarchy and landmarks
- **ARIA Labels**: Screen reader support for complex components
- **Keyboard Navigation**: Full keyboard accessibility
- **Focus Management**: Clear focus indicators

### Inclusive Design
- **High Contrast**: Sufficient color contrast ratios
- **Scalable Text**: Responsive to user font size preferences
- **Alternative Text**: Descriptive alt text for images and charts
- **Error Handling**: Clear, helpful error messages

## 🧪 Testing Approach

### Browser Testing
- **Cross-Browser**: Chrome, Firefox, Safari, Edge
- **Mobile Testing**: iOS Safari, Chrome Mobile
- **Responsive Testing**: Various screen sizes and orientations

### Performance Testing
- **Lighthouse Audits**: Regular performance monitoring
- **Core Web Vitals**: Tracking loading, interactivity, and visual stability
- **Network Testing**: Performance on slower connections

## 🔮 Future Enhancements

### Potential Improvements
1. **Component Library**: Formalize component system with documentation
2. **CSS Framework**: Consider CSS-in-JS or component-based styling
3. **Progressive Web App**: Add PWA capabilities for offline use
4. **Advanced Animations**: Micro-interactions for better UX
5. **Dark Mode**: Theme switching capability
6. **Internationalization**: Multi-language support

### Technology Considerations
- **Build Pipeline**: Consider adding Webpack or Vite for asset optimization
- **CSS Preprocessing**: Sass/SCSS for advanced styling features
- **JavaScript Framework**: Evaluate Vue.js or Alpine.js for enhanced interactivity
- **Component Testing**: Add Storybook for component development 