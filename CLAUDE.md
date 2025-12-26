# Custom Modes for Roo Code - Claude Code System Reference

This file contains project structure, configuration details, and development guidelines for the Custom Modes for Roo Code repository. Claude Code automatically loads this on startup.

---

## Project Overview

**Repository**: Custom Modes for Roo Code
**GitHub URL**: https://github.com/jtgsystems/Custom-Modes-Roo-Code
**Owner**: JTG Systems (https://jtgsystems.com)
**License**: MIT License
**Version**: 2025.1
**Status**: Active and Maintained
**Primary Language**: YAML (Configuration), Python (Tooling)

### Description
A comprehensive collection of specialized AI agent configurations for Roo Code, designed for modern software development following 2025 security-first principles and best practices. This project includes Python utilities for validation, conversion, and management of custom modes.

### Key Statistics
- **Total Agents**: 171+ specialized configurations
- **Agent Files**: 232 YAML files
- **Python Scripts**: 2 utility scripts
- **Repository Size**: ~2.5MB
- **Categories**: 9 major agent categories
- **Security Standard**: 2025 Security-First Architecture

---

## Repository Structure

### Root Directory
```
/tmp/repo-updates/Custom-Modes-Roo-Code/
├── agents/                    # All agent configurations (232 YAML files)
├── assets/                    # Banner images and visual assets
├── schemas/                   # JSON schema for validation
├── scripts/                   # Python validation and utility scripts
│   └── validate_custom_modes.py    # YAML validation script (195 lines)
├── vs-code/                   # VS Code specific tools and documentation
│   ├── convert_modes.py            # Mode conversion utility (625 lines)
│   └── README.md                   # VS Code integration guide
├── .vscode/                   # VS Code configuration
├── banner.png                 # Repository banner image
├── CLAUDE.md                  # Claude Code system reference (this file)
├── README.md                  # Main documentation (12KB)
├── CONTRIBUTING.md            # Contribution guidelines (6.9KB)
├── SECURITY.md                # Security policy (6.3KB)
├── LICENSE                    # MIT License
├── .gitignore                 # Git ignore patterns
└── researched.md              # Research documentation (18KB)
```

### Agent Categories Structure
```
agents/
├── ai-ml/                     # AI & Machine Learning (11 agents)
├── business-product/          # Business & Product (15 agents)
├── core-development/          # Core Development (36 agents)
├── infrastructure-devops/     # Infrastructure & DevOps (14 agents)
├── language-specialists/      # Language Specialists (23 agents)
│   ├── python/
│   ├── javascript/
│   ├── typescript/
│   ├── rust/
│   ├── golang/
│   ├── java/
│   ├── csharp/
│   └── general/
├── legal-compliance/          # Legal & Compliance (14 agents)
├── meta-orchestration/        # Meta-Orchestration (28 agents)
├── security-quality/          # Security & Quality (13 agents)
│   ├── security-audit/
│   ├── testing/
│   ├── compliance/
│   └── general/
└── specialized-domains/       # Specialized Domains (17 agents)
```

---

## Agent Configuration Schema

### Standard YAML Structure
All agents follow this standardized format:

```yaml
slug: agent-identifier          # Unique kebab-case identifier
name: "🔧 Agent Display Name"   # UI display name with optional emoji
category: category-name         # Primary category classification
subcategory: subcategory-name   # Optional subcategory
roleDefinition: |               # Detailed role and capabilities
  Multi-line description of agent responsibilities
customInstructions: |           # Comprehensive instructions
  Detailed workflow guidelines and best practices
groups:                         # Tool access permissions
  - read                        # File reading access
  - edit                        # File editing access
  - browser                     # Web browser access
  - command                     # Command execution
  - mcp                         # MCP server access
version: "2025.1"              # Version compliance
lastUpdated: "2025-09-20"      # Last modification date
```

### Permission Groups
- **read**: Access to read files and directories
- **edit**: Permission to modify files (can include regex restrictions)
- **browser**: Web browsing and search capabilities
- **command**: Terminal command execution
- **mcp**: MCP (Model Context Protocol) server integration

### Edit Permissions with Restrictions
```yaml
groups:
  - read
  - [edit, {fileRegex: "\\.(ts|js|json)$", description: "TypeScript/JavaScript files only"}]
  - command
```

---

## Python Tooling and Utilities

This repository includes sophisticated Python utilities for managing and converting custom modes. All Python code follows modern best practices with type hints, comprehensive error handling, and detailed documentation.

### 1. Validation Script: `scripts/validate_custom_modes.py`

**Purpose**: Validates custom_modes.yaml against Roo Code requirements
**Language**: Python 3.9+
**Lines of Code**: 195
**Dependencies**: `pyyaml`

**Key Features**:
- Schema-style validation matching Roo Code documentation
- Validates mode structure, permissions, and required fields
- Checks for duplicate slugs and invalid permission groups
- Supports rulesFiles validation with relativePath and content checks
- Type-safe implementation with type hints throughout
- Custom ValidationError exception for clear error reporting

**Validation Rules**:
- **Slug Pattern**: Must match `^[a-z0-9-]+$` (lowercase alphanumeric with hyphens)
- **Required Fields**: `slug`, `name`, `roleDefinition`, `groups`
- **Optional Fields**: `description`, `whenToUse`, `customInstructions`, `rulesFiles`
- **Permission Groups**: Must be from `{read, edit, browser, command, mcp}`
- **Edit Permissions**: Supports tuple syntax with fileRegex restrictions
- **Role Definition**: Minimum 10 characters
- **Name**: 1-100 characters

**Usage**:
```bash
# Validate default custom_modes.yaml
python3 scripts/validate_custom_modes.py

# Validate specific file
python3 scripts/validate_custom_modes.py path/to/custom_modes.yaml
```

**Implementation Highlights**:
- Uses `argparse` for CLI argument parsing
- Type-safe with Python 3.9+ type hints
- Comprehensive error messages with context
- Returns appropriate exit codes (0=success, 1=validation error, 2=file not found)
- Validates complex nested structures (groups tuples, rulesFiles)

### 2. Conversion Tool: `vs-code/convert_modes.py`

**Purpose**: Convert Roo Code CLI custom modes to VS Code compatible format
**Language**: Python 3.9+
**Lines of Code**: 625
**Dependencies**: `pyyaml`, `argparse`

**Key Features**:
- Multi-platform support (Windows, macOS, Linux)
- Intelligent mode merging (update existing, add new)
- XML rule file generation from customInstructions
- Automatic description and whenToUse generation
- Search functionality with wildcard support
- Direct VS Code settings integration (remote/local)
- Organized mode listing by alphabetical groups

**Commands**:

1. **List Modes**: Display all available modes organized alphabetically
   ```bash
   python3 vs-code/convert_modes.py list
   ```

2. **Search Modes**: Find modes with wildcard pattern matching
   ```bash
   python3 vs-code/convert_modes.py search python*
   python3 vs-code/convert_modes.py search *architect* *security*
   ```

3. **Convert Modes**: Transform CLI modes to VS Code format
   ```bash
   # Convert all modes
   python3 vs-code/convert_modes.py convert all

   # Convert specific modes
   python3 vs-code/convert_modes.py convert code-skeptic architect python-pro

   # Convert to custom output directory
   python3 vs-code/convert_modes.py convert all --output my_modes
   ```

4. **Purge Output**: Clean the converted modes directory
   ```bash
   python3 vs-code/convert_modes.py purge
   ```

5. **Copy to VS Code**: Install converted modes to VS Code
   ```bash
   # Copy to remote VS Code server
   python3 vs-code/convert_modes.py copy remote

   # Copy to local VS Code installation
   python3 vs-code/convert_modes.py copy local
   ```

**Implementation Highlights**:
- **Platform Detection**: Automatic VS Code settings path detection
  - Windows: `%APPDATA%/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings`
  - macOS: `~/Library/Application Support/Code/User/globalStorage/...`
  - Linux: `~/.config/Code/User/globalStorage/...`
  - Remote: `~/.vscode-server/data/User/globalStorage/...`

- **Filename Sanitization**: Converts mode names to safe filenames
  - Strips special characters
  - Converts to lowercase
  - Replaces spaces with underscores
  - Limits to 50 characters

- **Smart Description Generation**:
  - Extracts first 1-2 sentences from roleDefinition
  - Creates concise, meaningful summaries
  - Falls back to default if roleDefinition is missing

- **WhenToUse Auto-generation**:
  - Analyzes roleDefinition patterns
  - Converts "You are X" to "Activate when you need X"
  - Adds grammatically correct indefinite articles (a/an)
  - Preserves existing whenToUse if already defined

- **XML Rule File Generation**:
  - Converts customInstructions to XML format
  - Handles newline conversion for readability
  - Creates organized `.roo/rules-{slug}/` directories
  - Names files as `1_instructions.xml`

- **Intelligent Merging**:
  - Preserves existing modes not being converted
  - Updates modes that already exist in output
  - Adds new modes without duplicates
  - Reports update/add/keep statistics

- **YAML Formatting**:
  - Fixes PyYAML indentation issues
  - Maintains consistent 2-space indentation
  - Preserves mode order
  - Unicode-aware output

**Error Handling**:
- File not found errors with helpful messages
- YAML parsing errors with context
- Invalid slug detection and warnings
- IO error handling for file operations
- Platform-specific path validation

### 3. JSON Schema: `schemas/custom_modes.schema.json`

**Purpose**: JSON Schema for custom mode validation
**Reference**: https://docs.roocode.com/schemas/custom-modes.schema.json
**Validates**: Mode structure, permissions, required fields, data types

---

## Key Files and Configurations

### Python Requirements

**Python Version**: 3.9 or higher recommended
**Required Packages**:
- `pyyaml` - YAML parsing and generation
- `argparse` - Command-line argument parsing (standard library)
- `pathlib` - Path operations (standard library)
- `typing` - Type hints (standard library)

**Installation**:
```bash
# Install required dependencies
pip install pyyaml

# Or using a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pyyaml
```

### Configuration Files

All configuration paths have been updated for the new location at `/tmp/repo-updates/Custom-Modes-Roo-Code/`

---

## Agent Categories Deep Dive

### 1. AI & Machine Learning (11 agents)
**Location**: `agents/ai-ml/`
**Focus**: AI/ML development, deployment, and optimization
- Machine Learning Engineers
- AI System Architects
- Data Science Specialists
- MLOps Engineers
- Computer Vision Experts
- NLP Specialists
- LLM Integration Specialists

### 2. Business & Product (15 agents)
**Location**: `agents/business-product/`
**Focus**: Business strategy and product development
- Product Managers
- Business Analysts
- Marketing Specialists
- Sales Engineers
- Content Strategists

### 3. Core Development (36 agents)
**Location**: `agents/core-development/`
**Focus**: Foundation development roles and architectures
- Full-Stack Developers
- Backend Specialists
- Frontend Experts
- System Architects
- API Designers
- Integration Specialists

### 4. Infrastructure & DevOps (14 agents)
**Location**: `agents/infrastructure-devops/`
**Focus**: Cloud infrastructure and deployment
- Cloud Engineers (AWS, Azure, GCP)
- Kubernetes Specialists
- Docker Experts
- Monitoring & Observability
- Network Engineers

### 5. Language Specialists (23 agents)
**Location**: `agents/language-specialists/`
**Focus**: Programming language expertise

**Python** (agents/language-specialists/python/)
- FastAPI, Django, asyncio mastery
- Data processing and ML pipelines
- Performance optimization

**JavaScript/TypeScript** (agents/language-specialists/javascript/, typescript/)
- React, Node.js, Next.js
- Modern JavaScript features
- TypeScript type safety

**Rust** (agents/language-specialists/rust/)
- Systems programming
- WebAssembly development
- Memory safety focus

**Go** (agents/language-specialists/golang/)
- Microservices architecture
- Concurrent systems
- High-performance applications

**Java** (agents/language-specialists/java/)
- Spring Boot
- Enterprise systems
- JVM optimization

**C#** (agents/language-specialists/csharp/)
- .NET development
- Azure integration
- Enterprise applications

### 6. Legal & Compliance (14 agents)
**Location**: `agents/legal-compliance/`
**Focus**: Regulatory and legal expertise
- GDPR Compliance specialists
- Security Auditing
- Legal Documentation
- Regulatory Analysis
- US and Canada specific agents

**Example agents**:
- corporate-law-usa.yaml / corporate-law-canada.yaml
- employment-law-usa.yaml / employment-law-canada.yaml
- compliance-auditor-usa.yaml / compliance-auditor-canada.yaml
- intellectual-property-usa.yaml / intellectual-property-canada.yaml

### 7. Meta-Orchestration (28 agents)
**Location**: `agents/meta-orchestration/`
**Focus**: System coordination and workflow management
- Workflow Orchestrators
- Project Coordinators
- System Monitors
- Process Optimizers
- Integration Managers

### 8. Security & Quality (13 agents)
**Location**: `agents/security-quality/`
**Focus**: Security-first development and QA

**Subdirectories**:
- `security-audit/` - Security auditing specialists
- `testing/` - Testing and QA experts
- `compliance/` - Compliance verification
- `general/` - General security/quality roles

**Capabilities**:
- Cybersecurity Experts
- Penetration Testers
- Security Auditors
- Accessibility Specialists
- Compliance Officers

### 9. Specialized Domains (17 agents)
**Location**: `agents/specialized-domains/`
**Focus**: Industry-specific expertise
- **Fintech**: Financial systems, compliance
- **Gaming**: Game development, engines
- **Blockchain**: Smart contracts, DeFi
- **IoT**: Edge computing, sensors
- **SEO**: Search optimization, analytics

---

## Example Agent: Python Developer

**File**: `agents/language-specialists/python/python-developer.yaml`

```yaml
slug: python-developer
name: 🐍 Python Developer
category: language-specialists
subcategory: python
roleDefinition: |
  You are an elite Python Developer with optimization capabilities.
  You master FastAPI, Django, asyncio, data processing, machine learning
  pipelines, and performance optimization to build scalable Python
  applications with 10-100x performance improvements.

customInstructions: |
  # Python Developer Protocol

  ## 2025 PYTHON STANDARDS

  BEST PRACTICES:
  - Modern Python: Python 3.9+ with type hints and dataclasses
  - Async Programming: asyncio, aiohttp for high-performance
  - Framework Mastery: FastAPI for APIs, Django for web apps
  - Testing Excellence: pytest, coverage, property-based testing
  - Performance Optimization: Profiling, caching, algorithms

  AVOID:
  - Blocking I/O in async code
  - Ignoring type hints and static analysis
  - Poor error handling and logging
  - Inefficient algorithms and data structures
  - Security vulnerabilities (SQL injection, XSS)

groups:
  - read
  - edit
  - browser
  - command
  - mcp

version: "2025.1"
lastUpdated: "2025-09-20"
```

---

## Featured Custom Modes (from custom_modes.yaml)

### 1. Code Skeptic (slug: code-skeptic)
**Name**: 🧐 Code Skeptic
**Purpose**: Critical code quality inspector who questions everything
**Key Features**:
- Demands proof for all "it works" claims
- Catches shortcuts and laziness
- Enforces incremental improvements
- Reports what agents couldn't do
- Enforces project rules strictly

**Motto**: "Show me the logs or it didn't happen."

### 2. Architect (slug: architect)
**Name**: 🏗️ Architect
**Purpose**: Design scalable, secure, modular architectures
**Methodology**: SPARC (Specification → Implementation → Architecture → Refinement → Completion)
**Key Features**:
- Modular design with clear boundaries
- No hardcoded secrets or env values
- Security-first approach
- Performance-optimized data flows
- Framework currency protocol (uses Context7 MCP)
- Clean Architecture principles
- Technology architecture patterns

**Quality Gates**:
- Modular design with clear boundaries
- Extensible architecture patterns
- Performance optimization standards
- Clean architecture principles
- Technology architecture patterns

---

## Security Standards (2025)

### Core Security Principles
All agents implement 2025 Security-First Standards:

- ✅ **Zero-Trust Architecture** - Never trust, always verify
- ✅ **Secure by Default** - Secure configurations out of the box
- ✅ **OWASP Top 10 Compliance** - Industry standard security
- ✅ **Supply Chain Security** - Secure dependencies
- ✅ **Container Security** - Docker/Kubernetes security
- ✅ **API Security Best Practices** - Secure API design

### Required Security Features
```yaml
security_features:
  - input_validation
  - output_sanitization
  - secure_coding_practices
  - vulnerability_scanning
  - dependency_checking
  - secrets_management
```

### Security Reporting
**Contact**: security@jtgsystems.com
**Policy**: See SECURITY.md for vulnerability reporting procedures

---

## Installation and Usage

### Prerequisites
- **Roo Code** CLI tool installed
- **Git** for repository management
- **Node.js 18+** (recommended)
- **Python 3.9+** (for AI/ML agents)

### Installation Methods

#### Method 1: Full Installation
```bash
git clone https://github.com/jtgsystems/Custom-Modes-Roo-Code.git
cd Custom-Modes-Roo-Code
cp -r agents ~/.roo-code/custom-modes/
```

#### Method 2: Selective Installation
```bash
# Install specific category
cp -r agents/core-development ~/.roo-code/agents/

# Install specific agent
cp agents/language-specialists/python/python-developer.yaml ~/.roo-code/agents/
```

#### Method 3: Direct Download
```bash
curl -O https://raw.githubusercontent.com/jtgsystems/Custom-Modes-Roo-Code/main/agents/core-development/general/python-developer.yaml
```

### Basic Usage
```bash
# List available agents
ls agents/core-development/general/

# Configure Roo Code
roo-code config set agent-path agents/python-developer.yaml

# Activate agent
roo-code activate python-developer
```

### Advanced Configuration
```yaml
agent_config:
  base: "python-developer"
  customizations:
    frameworks: ["FastAPI", "Pydantic", "SQLAlchemy"]
    deployment: "docker"
    testing: "pytest"
    ci_cd: "github-actions"
```

---

## Development Workflow

### Contributing Guidelines
See CONTRIBUTING.md for detailed contribution guidelines.

### Agent Submission Process
1. **Fork the Repository**
   ```bash
   git fork https://github.com/jtgsystems/Custom-Modes-Roo-Code.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-agent
   ```

3. **Add Your Agent**
   ```bash
   cp template.yaml agents/category/subcategory/your-agent.yaml
   ```

4. **Validate Configuration**
   ```bash
   python scripts/validate_custom_modes.py
   ```

5. **Submit Pull Request**

### Quality Standards
- **Security First**: All agents must pass security validation
- **Performance**: Optimized for fast initialization
- **Documentation**: Clear, comprehensive descriptions
- **Testing**: Validated with real-world scenarios

---

## Git Configuration

### Repository Details
- **Remote**: origin (https://github.com/jtgsystems/Custom-Modes-Roo-Code.git)
- **Branch**: main
- **Latest Commit**: ee21815 (feat: update to clean stacked layers banner)

### Recent Commits
```
ee21815 - feat: update to clean stacked layers banner
a01aeba - feat: upgrade to V3 Quality banner and add star CTA
67dc3c3 - feat: add professional banner image to README
d82e845 - docs: add SEO keyword cloud
3133998 - fix: update broken links in README.md
5d3b84e - chore: add essential project files and documentation
```

### Untracked Files
```
assets/banner-old.png
assets/banner-robot-old.png
assets/banner-v3-quality-1.png
assets/banner-v3-quality-2.png
assets/banner-v3-quality_2025-10-22T08-37-54-874Z.png
```

---

## Project Architecture Patterns

### SPARC Methodology
Used by Architect mode and recommended for all development:
1. **Specification**: Clarify requirements and constraints
2. **Implementation**: Design high-level architecture
3. **Architecture**: Create detailed diagrams and integration points
4. **Refinement**: Optimize for performance, security, maintainability
5. **Completion**: Document final architecture

### Clean Architecture Principles
- **Separation of Concerns**: Clear boundaries between layers
- **Dependency Inversion**: High-level modules independent of low-level
- **Single Responsibility**: One reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Interface Segregation**: Clients depend only on what they use
- **Domain-Driven Design**: Focus on business domain

### Technology Architecture Patterns
- **Microservices**: Domain-driven design, API gateways, service mesh
- **Serverless**: AWS Lambda, Azure Functions, event-driven
- **Event-Driven**: Kafka, RabbitMQ, event sourcing, CQRS
- **Container Orchestration**: Kubernetes, Docker Swarm
- **API Design**: REST, GraphQL, gRPC, OpenAPI
- **Database Patterns**: CQRS, Event Sourcing, Polyglot persistence

---

## MCP Integration

### Context7 Integration
Several agents (especially Architect) use Context7 MCP for framework currency:
- `context7.resolve-library-id` - Get library identifiers
- `context7.get-library-docs` - Fetch up-to-date documentation

### Framework Currency Protocol
Process for ensuring latest framework versions:
1. Enumerate all frameworks, libraries, runtimes
2. Use Context7 to confirm latest stable versions
3. Record target versions in architecture specs
4. Flag deprecated SDKs and recommend migrations

---

## Related Resources

### Official Links
- **Repository**: https://github.com/jtgsystems/Custom-Modes-Roo-Code
- **Company**: https://jtgsystems.com
- **Support Email**: support@jtgsystems.com
- **Security Email**: security@jtgsystems.com

### External Resources
- **Roo Cline Extension**: [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=RooCline.roo-cline)
- **Roo Code Documentation**: https://docs.roocode.com
- **VS Code**: https://code.visualstudio.com

### Support Channels
- **GitHub Issues**: https://github.com/jtgsystems/Custom-Modes-Roo-Code/issues
- **GitHub Discussions**: https://github.com/jtgsystems/Custom-Modes-Roo-Code/discussions

---

## SEO Keywords

`openai` `codex` `claude` `roo` `code` `ai` `agent` `configurations` `yaml` `security` `devops` `automation` `workflow` `orchestration` `mlops` `machine` `learning` `fintech` `gaming` `compliance` `developer` `productivity` `vscode` `extension` `templates` `toolkit` `multiagent` `architecture` `integration` `pipelines` `testing` `monitoring` `observability` `cloud` `kubernetes` `docker` `python` `javascript` `typescript` `rust` `golang` `java` `csharp` `gdpr` `governance` `practices` `ultrathink` `optimization`

---

## Quick Reference Commands

### Repository Management
```bash
# Navigate to repository
cd /tmp/repo-updates/Custom-Modes-Roo-Code

# Check status
git status

# Update from remote
git pull origin main

# View agent structure
ls -la agents/

# Count agents
find agents -name "*.yaml" | wc -l

# Validate configuration
python3 scripts/validate_custom_modes.py
```

### Python Tooling Commands

#### Validation
```bash
# Validate default custom_modes.yaml
python3 scripts/validate_custom_modes.py

# Validate specific YAML file
python3 scripts/validate_custom_modes.py agents/core-development/general/python-developer.yaml
```

#### Mode Conversion and Management
```bash
# List all available modes
python3 vs-code/convert_modes.py list

# Search for specific modes
python3 vs-code/convert_modes.py search python*
python3 vs-code/convert_modes.py search *security* *audit*

# Convert all modes to VS Code format
python3 vs-code/convert_modes.py convert all

# Convert specific modes
python3 vs-code/convert_modes.py convert code-skeptic architect python-developer

# Convert with custom output directory
python3 vs-code/convert_modes.py convert all --output custom_output

# Purge converted modes directory
python3 vs-code/convert_modes.py purge

# Copy to VS Code (remote environment)
python3 vs-code/convert_modes.py copy remote

# Copy to VS Code (local environment)
python3 vs-code/convert_modes.py copy local
```

#### Python Development Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install pyyaml

# Run validation tests
python3 scripts/validate_custom_modes.py

# Run conversion with help
python3 vs-code/convert_modes.py --help
```

### Agent Development
```bash
# Copy template
cp agents/template.yaml agents/category/new-agent.yaml

# Edit agent
nano agents/category/new-agent.yaml

# Validate
python3 scripts/validate_custom_modes.py

# Test with Roo Code
roo-code validate agents/category/new-agent.yaml
```

### GitHub Operations
```bash
# View repository
gh repo view jtgsystems/Custom-Modes-Roo-Code

# Create issue
gh issue create -R jtgsystems/Custom-Modes-Roo-Code

# Create PR
gh pr create -R jtgsystems/Custom-Modes-Roo-Code
```

---

## File Size Limits and Best Practices

### Recommended Limits
- **Agent Files**: < 500 lines per YAML
- **Documentation**: Modular, focused files
- **No Secrets**: Never commit credentials or API keys
- **English Only**: All comments and documentation in English

### Code Quality Standards
- **Type Safety**: Use type hints (Python), TypeScript
- **Testing**: Comprehensive test coverage
- **Security**: 2025 security standards compliance
- **Performance**: Optimized for production use
- **Documentation**: Clear, comprehensive inline docs

---

## License

**MIT License**

Copyright (c) 2025 JTG Systems

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

---

## Acknowledgments

- **Roo Code Team** - For the amazing development platform
- **Open Source Community** - For continuous inspiration
- **Contributors** - For making this project possible
- **Security Researchers** - For ensuring robust security standards

---

**Built with care by [JTG Systems](https://github.com/jtgsystems)**

**Following 2025 Security-First Development Standards**

*Last Updated: 2025-12-26*
*System: Linux*
*Repository Path: /tmp/repo-updates/Custom-Modes-Roo-Code/*

## Python Project Information

### Technology Stack
- **Python**: 3.9+ recommended
- **YAML Processing**: PyYAML library
- **Type Safety**: Full type hints using Python typing module
- **CLI Framework**: argparse (standard library)
- **Path Operations**: pathlib (standard library)
- **Platform Support**: Cross-platform (Windows, macOS, Linux)

### Code Quality Standards
- **Type Hints**: All functions use type annotations
- **Error Handling**: Comprehensive try-except blocks
- **Documentation**: Detailed docstrings for all modules and functions
- **Validation**: Schema validation for all configuration files
- **Exit Codes**: Proper Unix exit codes (0=success, 1=error, 2=file not found)
- **Logging**: Structured logging using Python logging module

### Python Scripts Overview

1. **validate_custom_modes.py** (195 lines)
   - Validates YAML configuration files
   - Ensures compliance with Roo Code schema
   - Checks for duplicate slugs and invalid permissions
   - Returns detailed error messages with context

2. **convert_modes.py** (625 lines)
   - Converts CLI modes to VS Code format
   - Multi-command interface (list, search, convert, purge, copy)
   - Platform-aware VS Code settings path detection
   - Intelligent YAML merging and formatting
   - XML rule file generation

### Dependencies
```
pyyaml>=6.0  # YAML parsing and generation
```

### Development Environment Setup
```bash
# Clone repository
git clone git@github.com:jtgsystems/Custom-Modes-Roo-Code.git
cd Custom-Modes-Roo-Code

# Set up Python environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pyyaml

# Verify installation
python3 scripts/validate_custom_modes.py --help
python3 vs-code/convert_modes.py --help
```

