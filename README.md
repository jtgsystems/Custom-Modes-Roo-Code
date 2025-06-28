# Custom Roo Code Modes 🚀

Welcome to the **Custom Roo Code Modes** repository! 🎉 This project serves as a central place to store, manage, and share custom mode definitions for the [Roo Code](https://github.com/RooVetGit/Roo-Code) AI agent within Visual Studio Code.

## 🌟 Overview

Roo Code utilizes specialized AI "modes" or personas to tackle different development tasks. This repository contains a curated collection of these mode definitions, primarily stored in the `custom_modes.json` file. By maintaining these definitions here, we can version control, share, and collaboratively refine the capabilities of various AI assistants used in the Roo Code workflow.

### Key Goals 🎯
- **Centralized Mode Management**: Provide a single source of truth for custom Roo Code mode configurations.
- **Enhanced AI Capabilities**: Define specialized roles and detailed instructions to improve AI performance on specific tasks (e.g., frontend development, SEO, content strategy).
- **Workflow Optimization**: Tailor AI assistants to specific project needs and best practices.
- **Collaboration**: Facilitate sharing and improvement of mode definitions within a team or community.
- **Self-Correction Tracking**: Log errors and corrections applied to modes over time in `botcorrections.json`.

## ✨ Mode Examples Included

This repository contains definitions for various modes, including (but not limited to):

### 🤖 Standard Development Modes
- **`full-stack-developer`**: Expert in comprehensive web application development
- **`frontend-developer`**: Specialist in creating modern web interfaces
- **`devops-engineer`**: Infrastructure automation and deployment expert
- **`content-strategist`**: SEO-aware content creation and strategy
- **`seo-specialist`**: Comprehensive on-page and technical SEO optimization
- **`compliance-specialist`**: Regulatory adherence and risk management
- **`web-design-specialist`**: ⭐ **NEW** - Web Design ULTRON with comprehensive quality gates and enterprise standards

### 🎨 NEW: Web Design Specialist ULTRON Mode
- **`web-design-specialist`**: Revolutionary web design mode with enterprise-grade quality gates
  - **🚪 Quality Gate Enforcement**: ALL code must pass 70+ score, 0 critical violations
  - **♿ WCAG 2.1 AA Compliance**: Mandatory accessibility standards enforcement
  - **⚡ Core Web Vitals**: LCP <2.5s, FID <100ms, CLS <0.1 optimization
  - **📱 Mobile-First Design**: Responsive design starting from 320px
  - **🔒 Security Standards**: CSP headers, HTTPS, input validation
  - **🧪 Automated Testing**: HTML/CSS validation, Lighthouse audits, cross-browser testing
  - **🛠️ Tool Integration**: Web design quality gates, flaw detection, bot validation
  - **📋 100+ Item Checklist**: Comprehensive coverage from HTML foundation to analytics

### 🚀 Claude Code ULTRON Mode
- **`claude-code-ultron`**: Elite software engineer with MCP orchestration capabilities
  - **25+ Department Organization**: Structured workspace with SECURITY, OPERATIONS, DEVELOPMENT
  - **12+ MCP Tools**: Unified Thinking (33 frameworks), Research, Image Processing, etc.
  - **Performance Optimization**: 2-50x speed improvements with parallel processing
  - **Security Integration**: KEYHOLDER scanning, VAULT credential management
  - **Auto-Launch Systems**: Session start protocols and health monitoring
  - **Military-Grade Discipline**: Systematic automation and precision execution

### 📋 Project Management Modes
- **`product-owner`**: End-to-end project management and client engagement
- **`software-architect`**: Scalable MVP architecture design
- **`tech-lead`**: Task decomposition and technical specification
- **`full-stack-implementer`**: Modular, production-ready implementation
- **`code-monkey`**: Rapid development following tech lead guidance

Each mode definition includes:
- `slug`: A unique identifier.
- `name`: A human-readable name.
- `roleDefinition`: Describes the AI's persona and expertise.
- `customInstructions`: Detailed protocols and guidelines the mode should follow, including self-correction mandates.
- `groups`: Specifies the tool capabilities assigned to the mode (e.g., `read`, `edit`, `command`, `mcp`).

## 🛠️ Usage

To use these custom modes with your Roo Code VS Code extension:

1.  **Locate Roo Code Storage:** Find the Roo Code global storage directory. On Windows, this is typically:
    ```
    C:\\Users\\<YourUsername>\\AppData\\Roaming\\Code - Insiders\\User\\globalStorage\\rooveterinaryinc.roo-cline\\settings\\
    ```
    *(Adjust the path if you use the stable version of VS Code or a different operating system)*.

2.  **Copy Configuration:** Copy the appropriate `custom_modes.json` file from this repository into the `settings` directory found in step 1, replacing the existing file if necessary.

3.  **Restart VS Code:** Restart Visual Studio Code to ensure Roo Code loads the new mode definitions.

4.  **Select Mode:** You should now be able to select and use the custom modes defined in this repository within the Roo Code interface.

## 📁 Repository Structure

```
Custom-Modes-Roo-Code/
├── README.md                           # This documentation
├── cline_custom_modes.json            # Complete mode collection
├── NEW CUSTOM MODES.json              # Project management focused modes  
├── claude-code-ultron-mode.json       # Claude Code ULTRON mode definition
└── (additional mode files as needed)
```

## 🚀 Claude Code ULTRON Integration

The **Claude Code ULTRON** mode represents a revolutionary approach to AI-assisted development:

### Core Capabilities
- **MCP Tool Orchestration**: Seamlessly integrates 12+ specialized tools
- **Performance Optimization**: Implements 2-50x speed improvements through parallel processing
- **Security-First**: KEYHOLDER credential scanning and VAULT management
- **Autonomous Operation**: Self-managing workflows with minimal human intervention

### Session Start Protocol
```bash
# Auto-launch all MCP tools and verify system health
bash /workspace/SCRIPTS/automation/auto-launch-behavior.sh
bash /workspace/SCRIPTS/monitoring/ultra-fast-mcp-health-optimized.sh
```

### Tool Ecosystem
1. **Unified Thinking MCP** - 33 cognitive frameworks for complex problem solving
2. **Research MCP** - AI-powered web research with Google Custom Search
3. **Image Processing MCP** - Complete image toolkit with AI analysis
4. **KEYHOLDER Security** - Real-time credential leak detection
5. **VAULT System** - Centralized credential management
6. **Performance Monitoring** - Ultra-fast verification protocols

### Performance Standards
- **File Operations**: 400+ files/second minimum
- **Git Operations**: 1000+ files/second target  
- **Health Checks**: Sub-3-second completion
- **Memory Usage**: Optimized garbage collection
- **Parallel Processing**: Maximum CPU utilization

## 🤝 Contributing

Contributions are welcome! If you improve an existing mode or create a new useful one, feel free to submit a Pull Request. Please ensure:

- The JSON format is valid.
- Instructions are clear and follow the established pattern (including Information Verification and Self-Correction clauses).
- The `botcorrections.json` file is updated if the changes stem from a logged correction.
- Performance optimization protocols are included for development modes.
- Security considerations are addressed for modes handling sensitive operations.

## 🎨 Web Design Specialist Checklist

The **Web Design Specialist ULTRON** mode includes a comprehensive 100+ item checklist organized by priority:

### 🚨 CRITICAL ITEMS
- ✅ HTML5 doctype, UTF-8 charset, responsive viewport
- ♿ WCAG 2.1 AA compliance (screen readers, keyboard navigation)
- 🔒 Security compliance (CSP headers, HTTPS, input validation)
- 📱 Semantic HTML structure with proper ARIA labels

### ⚡ HIGH PRIORITY ITEMS  
- 🎯 CSS excellence (external files, custom properties, mobile-first)
- 📊 Performance optimization (Core Web Vitals, image optimization)
- 📱 Responsive design (320px+ breakpoints, touch-friendly UI)
- 🧪 Testing & validation (W3C validation, cross-browser testing)

### 🔧 MEDIUM PRIORITY ITEMS
- 🎨 UI/UX excellence (design systems, typography, animations)  
- 🛠️ Development standards (version control, documentation, testing)

### 📈 LOW PRIORITY ITEMS
- 📊 Analytics & monitoring (GA4, error tracking, performance monitoring)

### 🛠️ INTEGRATED TOOLS
```bash
# Quality gate validation
python3 /home/ultron/workspace/TOOLS/production/web-design-quality-gates.py validate <file>

# Automated flaw detection  
python3 /home/ultron/workspace/TOOLS/production/web-design-flaw-detector-enhanced.py <url>

# Bot code validation
from bot_web_code_validator import validate_bot_generated_code
```

## 🔒 Security Considerations

When using modes that handle sensitive data or operations:

- Always use VAULT system for credential management
- Run KEYHOLDER security scans before commits
- Follow department naming conventions (CAPITALS for department names)
- Implement proper error handling and validation
- Use parallel processing for performance optimization

## 📄 License

*(Optional: Specify a license here if you wish, e.g., MIT License)*

---

**Note**: The Claude Code ULTRON mode requires the complete ULTRON Project workspace setup with all MCP tools properly configured. Standard Roo Code modes will work with any Roo Code installation.