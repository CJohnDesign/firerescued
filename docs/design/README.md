# Fire Rescued Design System

A comprehensive design system for the Fire Rescued burnout prevention platform, built on health-focused design principles and accessibility standards.

## 🎨 Design Philosophy

### Core Principles
1. **Health-Focused**: Colors and interactions that promote wellness and calm
2. **Data-Driven**: Clear visualization of complex health metrics
3. **Accessible**: WCAG 2.1 AA compliant for all users
4. **Consistent**: Unified visual language across all touchpoints
5. **Responsive**: Seamless experience across all devices

### Visual Language
- **Modern & Clean**: Minimalist approach that reduces cognitive load
- **Apple-Inspired**: Familiar patterns with health app conventions
- **Calming Palette**: Colors that reduce stress and promote wellbeing
- **Readable Typography**: Optimized for data comprehension

## 🎯 Target Audience Design Considerations

### Primary Users: Healthcare Workers & High-Stress Professionals
- **Cognitive Load**: Simplified interfaces for tired users
- **Quick Scanning**: Information hierarchy for rapid assessment
- **Error Prevention**: Clear states and confirmation patterns
- **Professional Feel**: Trustworthy, medical-grade appearance

## 📐 Layout System

### Grid System
- **Base**: Bootstrap 5's 12-column responsive grid
- **Containers**: Max-width 1400px for optimal readability
- **Breakpoints**: Mobile-first responsive design
- **Spacing**: 8px base unit for consistent rhythm

### Layout Patterns
```css
.dashboard-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0.5rem;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

## 🔗 Component References

- [**Color Palette**](./colors.md) - Complete color system with usage guidelines
- [**Typography**](./typography.md) - Font hierarchy and text styling
- [**Components**](./components.md) - UI component library and specifications
- [**Icons**](./icons.md) - Icon system and usage patterns
- [**Spacing**](./spacing.md) - Spacing scale and layout principles

## 🏗️ Design Tokens

### CSS Custom Properties
```css
:root {
    /* Colors */
    --primary-color: #4361ee;
    --secondary-color: #7209b7;
    --success-color: #38b000;
    --warning-color: #f9c74f;
    --danger-color: #ef476f;
    --neutral-color: #adb5bd;
    
    /* Layout */
    --border-radius: 10px;
    --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    --transition-speed: 0.3s;
    
    /* Typography */
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --heading-weight: 600;
    --body-weight: 400;
}
```

## 📱 Responsive Behavior

### Breakpoint Strategy
- **Mobile**: < 768px - Single column, stacked components
- **Tablet**: 768px - 1024px - Two column layout, condensed navigation
- **Desktop**: > 1024px - Full three column layout, expanded features

### Adaptive Components
- **Navigation**: Collapsible hamburger menu on mobile
- **Cards**: Stack vertically on smaller screens
- **Charts**: Responsive sizing with touch interactions
- **Forms**: Single column on mobile, multi-column on desktop

## 🎨 Brand Application

### Logo Usage
- **Primary**: Full "Fire Rescued" wordmark
- **Icon**: Flame symbol for favicon and small applications
- **Colors**: Primary blue on light backgrounds, white on dark

### Voice & Tone
- **Professional**: Medical-grade accuracy and trust
- **Supportive**: Encouraging without being patronizing
- **Clear**: Direct communication about health data
- **Calm**: Reducing anxiety around health monitoring

## ♿ Accessibility Standards

### WCAG 2.1 AA Compliance
- **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Keyboard Navigation**: Full functionality without mouse
- **Screen Readers**: Proper ARIA labels and semantic HTML
- **Focus Management**: Clear focus indicators and logical tab order

### Inclusive Design Features
- **High Contrast Mode**: Enhanced visibility options
- **Text Scaling**: Responsive to user font size preferences
- **Motion Sensitivity**: Reduced motion options for vestibular disorders
- **Color Independence**: Information not conveyed by color alone

## 🔧 Implementation Guidelines

### CSS Architecture
- **BEM Methodology**: Block, Element, Modifier naming convention
- **Custom Properties**: CSS variables for theming and consistency
- **Mobile First**: Progressive enhancement approach
- **Modular CSS**: Component-based styling organization

### Component Development
1. **Start with Base**: Use Bootstrap base classes
2. **Add Custom Styling**: Layer custom properties and modifications
3. **Test Responsively**: Verify across all breakpoints
4. **Validate Accessibility**: Screen reader and keyboard testing

## 📋 Usage Examples

### Metric Cards
```html
<div class="metric-card primary-metric" style="--metric-color: var(--success-color);">
    <div class="metric-header">
        <div class="metric-icon">
            <i class="fas fa-heartbeat"></i>
        </div>
        <h3>Recovery Score</h3>
    </div>
    <div class="metric-value">87.2</div>
    <div class="metric-label">
        <span class="status-pill status-positive">Excellent</span>
    </div>
</div>
```

### Status Indicators
```html
<span class="status-pill status-positive">Low Risk</span>
<span class="status-pill status-neutral">Moderate</span>
<span class="status-pill status-negative">High Risk</span>
```

## 📊 Health Data Visualization Principles

### Color Coding for Health Metrics
- **Green (#38b000)**: Positive/healthy ranges
- **Yellow (#f9c74f)**: Caution/moderate ranges  
- **Red (#ef476f)**: Alert/concerning ranges
- **Gray (#adb5bd)**: No data/neutral states

### Chart Design Guidelines
- **Minimal Axes**: Reduce chart junk for clarity
- **Semantic Colors**: Health status colors throughout
- **Interactive Elements**: Hover states and tooltips
- **Responsive Sizing**: Adapt to container constraints

## 🔄 Design System Maintenance

### Version Control
- **Semantic Versioning**: Major.Minor.Patch for design tokens
- **Change Documentation**: Clear migration guides for updates
- **Backwards Compatibility**: Graceful deprecation of old patterns

### Review Process
1. **Design Review**: UX/UI team approval
2. **Accessibility Audit**: WCAG compliance check
3. **Development Review**: Implementation feasibility
4. **User Testing**: Validation with target users

## 🚀 Tools & Resources

### Design Tools
- **Figma**: Primary design and prototyping tool
- **Sketch**: Alternative design tool support
- **Adobe Color**: Color palette generation and testing

### Development Tools
- **CSS Custom Properties**: Dynamic theming support
- **PostCSS**: CSS processing and optimization
- **Stylelint**: CSS linting and standards enforcement

### Testing Tools
- **axe-core**: Automated accessibility testing
- **WAVE**: Web accessibility evaluation
- **Lighthouse**: Performance and accessibility audits
- **Color Oracle**: Color blindness simulation

## 📈 Metrics & Success Criteria

### Design System Adoption
- **Component Usage**: Percentage of UI using design system components
- **Consistency Score**: Visual consistency across pages
- **Developer Velocity**: Time to implement new features

### User Experience Metrics  
- **Accessibility Score**: WCAG compliance percentage
- **User Task Completion**: Success rate for key user flows
- **User Satisfaction**: Feedback on visual design and usability

---

**Version**: 1.0.0  
**Last Updated**: {{ now.strftime('%B %d, %Y') }}  
**Maintained by**: Fire Rescued Design Team 