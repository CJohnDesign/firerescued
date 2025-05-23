# Prompts Directory

This directory contains AI prompt configurations for the FireRescued application.

## Files

### `system_prompt.md`
Contains the main system prompt for the AI health analytics assistant. This prompt includes:

### `fallback_prompt.py`
Contains the fallback system prompt as an importable Python variable (`FALLBACK_SYSTEM_PROMPT`). This prompt includes:

- **Role Definition**: Professional health analytics AI assistant specializing in burnout prevention for firefighters and tactical athletes
- **Assessment Methodology**: Comprehensive methodology for determining recovery status
- **Recovery Zones**: Three-zone system (Red, Yellow, Green) with specific characteristics and goals
- **Recovery Practices**: Zone-specific physical recovery recommendations
- **Mind-Body Regulation**: Breathing and mindfulness techniques for each recovery zone
- **Scientific Basis**: Research-backed foundations for the assessment approach

## Usage

The system prompt is automatically loaded by the `BurnoutInsightsEngine` class in `app/services/ai_service.py`. The service includes error handling to fall back to a basic prompt if the file cannot be loaded.

## Editing Guidelines

When modifying prompts:

1. **Always add functionality, never remove** - Follow the custom instruction to only expand prompts, never simplify or condense
2. **Maintain scientific accuracy** - Ensure all recommendations are evidence-based
3. **Keep firefighter context** - Remember this is specifically designed for tactical athletes and shift workers
4. **Test thoroughly** - Verify AI responses maintain quality and relevance after changes
5. **Update documentation** - Reflect any major changes in this README

## File Structure

```
app/prompts/
├── README.md              # This documentation file
├── system_prompt.md       # Main AI system prompt
└── fallback_prompt.py     # Fallback prompt as importable variable
```

## Integration

The prompts are loaded using the `_load_system_prompt()` method in the AI service, which:
- Reads the markdown file from disk
- Includes error handling for missing files  
- Imports and uses the fallback prompt from `fallback_prompt.py`
- Logs loading status for debugging

This approach allows for easy prompt management and version control while maintaining system reliability. 