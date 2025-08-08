# CONTRADICTION LEDGER TEMPLATE - Research Protocol

## PURPOSE
Track and resolve conflicting information discovered during multi-provider research.

## CONTRADICTION TRACKING MATRIX

### Active Contradictions
| ID | Claim A | Source A | Tier A | Provider A | Claim B | Source B | Tier B | Provider B | Status | Confidence | Resolution Method |
|----|---------|----------|--------|------------|---------|----------|--------|------------|--------|------------|-------------------|
| C001 | [Specific claim] | [Source name] | A/B/C | research_mcp | [Conflicting claim] | [Source name] | A/B/C | web_search | ACTIVE | HIGH/MED/LOW | [Method to resolve] |
| C002 | [Specific claim] | [Source name] | A/B/C | browser_auto | [Conflicting claim] | [Source name] | A/B/C | research_mcp | RESOLVED | HIGH | [Resolution applied] |

### Resolution Strategies
1. **Source Authority**: Defer to higher-tier source (A > B > C)
2. **Temporal Priority**: Use more recent information
3. **Methodology Quality**: Evaluate research quality and sample size
4. **Consensus Building**: Weight of evidence across multiple sources
5. **Context Specificity**: Consider scope and applicability
6. **Expert Validation**: Seek additional expert opinions

### Contradiction Categories
- **FACTUAL**: Conflicting statistics, dates, or measurements
- **METHODOLOGICAL**: Different research approaches yielding different results
- **INTERPRETATIVE**: Same data interpreted differently
- **TEMPORAL**: Information that has changed over time
- **CONTEXTUAL**: Claims true in different contexts but appear contradictory

### Resolution Status Definitions
- **ACTIVE**: Contradiction identified but not yet resolved
- **INVESTIGATING**: Additional research being conducted
- **RESOLVED**: Satisfactory resolution achieved
- **UNRESOLVABLE**: Fundamental disagreement that cannot be resolved
- **CONTEXT-DEPENDENT**: Valid in different contexts

### Impact Assessment Scale
- **CRITICAL**: Affects core conclusions of research
- **MAJOR**: Affects significant findings or recommendations
- **MINOR**: Affects supporting details but not main conclusions
- **NEGLIGIBLE**: No impact on research outcomes

## EXAMPLE ENTRIES

### Resolved Contradiction Example
```markdown
**ID**: C001
**Claim A**: "AI productivity improvements average 40% in software development" 
**Source A**: McKinsey Global Institute Report 2024 [Tier A]
**Provider A**: research_mcp

**Claim B**: "AI productivity gains typically range 15-25% in development teams"
**Source B**: Stack Overflow Developer Survey 2024 [Tier B]  
**Provider B**: web_search

**Status**: RESOLVED
**Resolution Method**: Source Authority + Methodology Quality
**Resolution**: McKinsey study (Tier A) used larger sample size (10,000+ developers) vs Stack Overflow survey (5,000 developers). McKinsey included more advanced AI tools. Both valid but different scopes.
**Impact**: MINOR - Used McKinsey figure with caveat about tool sophistication
```

### Active Contradiction Example
```markdown
**ID**: C002
**Claim A**: "Memory-mapped file I/O provides 3-8x performance improvement"
**Source A**: Project optimization benchmarks [Tier B]
**Provider A**: research_mcp

**Claim B**: "Memory mapping shows 2-3x improvement in most real-world scenarios"  
**Source B**: Linux Kernel Documentation [Tier A]
**Provider B**: browser_automation

**Status**: INVESTIGATING
**Resolution Method**: Additional benchmarking required
**Notes**: Results may be optimized scenarios. Need broader performance data.
**Impact**: MAJOR - Affects performance optimization recommendations
```

## RESOLUTION WORKFLOW

### Step 1: Identification
- Detect contradictions during research synthesis
- Classify by category and assess impact
- Assign unique ID and track in matrix

### Step 2: Investigation  
- Examine source quality and methodology
- Look for additional sources to break ties
- Consider temporal and contextual factors

### Step 3: Resolution
- Apply appropriate resolution strategy
- Document reasoning and evidence
- Update research findings accordingly

### Step 4: Validation
- Verify resolution doesn't create new contradictions
- Check impact on overall research conclusions
- Update confidence levels as needed

## QUALITY METRICS

### Resolution Rate
- Target: >80% of contradictions resolved
- Critical contradictions: 100% must be addressed
- Unresolvable: <5% acceptable

### Source Quality Distribution
- Tier A sources should resolve most critical contradictions
- Tier B sources acceptable for moderate contradictions
- Tier C sources require additional validation

### Provider Coverage
- Each provider should contribute to contradiction resolution
- Cross-provider validation strengthens resolution confidence
- Single-provider contradictions require external validation

## REPORTING TEMPLATE

### Contradiction Summary
```markdown
**Total Contradictions Identified**: [Number]
**Resolved**: [Number] ([Percentage]%)
**Unresolved**: [Number] ([Percentage]%)
**Impact on Research Confidence**: [Assessment]

**Major Unresolved Contradictions**:
1. [ID]: [Brief description] - [Impact]
2. [ID]: [Brief description] - [Impact]

**Resolution Quality**: [High/Medium/Low based on evidence quality]
```