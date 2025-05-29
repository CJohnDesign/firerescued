# Issues Directory

This directory contains documented issues, bugs, research spikes, and feature requests for the Fire Rescued application.

## Issue Numbering

Issues are numbered sequentially starting from 001:
- `001-whoop-sync-no-data-token-investigation.md`
- `002-next-issue-title.md`
- etc.

## Issue Types

- **Bug**: Something that's broken and needs fixing
- **Research Spike**: Investigation needed before implementation
- **Feature**: New functionality to be added
- **Enhancement**: Improvement to existing functionality
- **Technical Debt**: Code quality improvements

## Priority Levels

- **Critical**: Blocking users, security issues
- **High**: Significant impact on user experience
- **Medium**: Important but not urgent
- **Low**: Nice to have, minor improvements

## Issue Template

```markdown
# Issue #XXX: [Title]

**Status:** [Open/In Progress/Resolved/Closed]  
**Type:** [Bug/Research Spike/Feature/Enhancement/Technical Debt]  
**Priority:** [Critical/High/Medium/Low]  
**Created:** YYYY-MM-DD  
**Assignee:** [Name or TBD]  

## Problem Statement
[Clear description of the issue or requirement]

## Current Behavior
[What happens now]

## Expected Behavior  
[What should happen]

## Technical Investigation Areas
[Specific areas of code or systems to investigate]

## Debug Steps to Investigate
[Actionable steps to reproduce or investigate]

## Expected Outcomes
[What we want to achieve]

## Related Files
[List of relevant files and their purposes]

## Potential Solutions
[Possible approaches to solve the issue]

## Next Steps
- [ ] Task 1
- [ ] Task 2

## Notes
[Additional context, decisions, or observations]
```

## Status Management

### Open
- Issue has been identified and documented
- Ready for investigation or implementation

### In Progress  
- Someone is actively working on the issue
- Should include updates on progress

### Resolved
- Issue has been fixed or completed
- Should include summary of solution implemented

### Closed
- Issue is complete and verified
- No longer needs attention

## File Naming Convention

Format: `XXX-brief-descriptive-title.md`

Examples:
- `001-whoop-sync-no-data-token-investigation.md`
- `002-dashboard-loading-performance.md`
- `003-user-authentication-refactor.md`

## Cross-References

When issues are related, reference them using the issue number:
- "Related to Issue #001"
- "Depends on Issue #005"
- "Duplicate of Issue #003"

## Resolution Documentation

When closing an issue, add a resolution section:

```markdown
## Resolution (Added: YYYY-MM-DD)

**Solution:** [Brief description of how it was fixed]
**PR/Commit:** [Link to pull request or commit hash]
**Verification:** [How the fix was tested]
**Impact:** [Any side effects or considerations]
``` 