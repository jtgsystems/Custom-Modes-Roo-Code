# 🚀 Custom Modes for Roo Code VS Code Extension

Enhanced AI coding assistance configurations using the SPARC methodology (Specification → Pseudocode → Architecture → Refinement → Completion).

## 📊 Overview

This repository contains **140+ AI specialist agents** and custom modes for Claude Code, Roo Code, and other AI-powered development tools. Each mode is designed with specific role definitions, quality gates, and best practices to enhance your development workflow.

## 🎯 Key Features

- **SPARC Methodology Integration**: Structured development workflow
- **Security-First Approach**: Built-in security standards and reviews
- **Performance Optimization**: Standards for scalability and efficiency
- **Clean Architecture**: Modular design principles
- **Comprehensive Testing**: TDD integration and quality gates
- **Professional Documentation**: Clear, comprehensive guides

## 📁 File Structure

```
├── custom-modes.yaml           # ✨ NEW: Proper YAML format for all modes
├── UPDATED-MODES              # Original modes file (932KB)
├── README.md                  # This documentation
├── .pre-commit-config.yaml    # Code quality hooks
└── AGENTS/                    # Directory structure (140 agents)
    ├── ai-ml-agents/          (11 agents)
    ├── language-specialists/  (23 agents)
    ├── infrastructure-devops/ (13 agents)
    ├── quality-security/      (15 agents)
    ├── business-product/      (11 agents)
    ├── development-core/      (13 agents)
    ├── specialized-domains/   (9 agents)
    ├── developer-experience/  (10 agents)
    ├── meta-orchestration/    (8 agents)
    ├── research-analysis/     (9 agents)
    ├── legal-compliance/      (5 agents)
    ├── special-modes/         (13 agents)
    ├── ALL_AGENTS_COMBINED.json
    ├── MASTER_INDEX.json
    └── README.md
```

## 🛠️ Core Custom Modes

### Primary Development Modes

| Mode | Description | Focus Area |
|------|-------------|------------|
| 🏗️ **Architect** | System design and architecture | Scalable, secure, modular architectures |
| 🧠 **Auto-Coder** | Clean, efficient code implementation | Modular code with clean architecture |
| 🧪 **Tester (TDD)** | Test-driven development | Red-Green-Refactor cycle |
| 🐛 **Debugger** | Issue troubleshooting and fixes | Systematic debugging approaches |
| 🔒 **Security Reviewer** | Security audits and best practices | OWASP Top 10, vulnerability assessment |
| 📚 **Documentation Writer** | Comprehensive documentation | API docs, user guides, architecture |

### Specialized Modes

- **Integration**: System integration and merging
- **Post-Deployment Monitoring**: Performance observation
- **Refinement Optimization**: System improvements
- **DevOps**: Infrastructure and deployment
- **Supabase Admin**: Database administration
- **MCP**: Model Context Protocol integration
- **SPARC**: Structured development methodology

## 🚀 Quick Start

### Using with Roo Code VS Code Extension

1. **Install the extension**: Get Roo Code from VS Code marketplace
2. **Load custom modes**: Import `custom-modes.yaml` into your workspace
3. **Select a mode**: Choose the appropriate specialist for your task
4. **Follow SPARC methodology**: Specification → Pseudocode → Architecture → Refinement → Completion

### Using with Claude Code

1. **Copy mode definitions**: Use the role definitions from `custom-modes.yaml`
2. **Apply custom instructions**: Follow the detailed guidelines for each mode
3. **Implement quality gates**: Ensure all checkboxes are met before completion

## 📋 SPARC Methodology

All modes follow the SPARC workflow:

1. **🎯 Specification**: Define requirements and constraints clearly
2. **📝 Pseudocode**: Create high-level logic with TDD anchors
3. **🏗️ Architecture**: Design modular, clean architecture patterns
4. **✨ Refinement**: Optimize for performance, security, and maintainability
5. **✅ Completion**: Test thoroughly and document with completion confirmation

## 🔒 Security Standards

Every mode includes built-in security considerations:

- ✅ No hardcoded secrets or environment values
- ✅ Input validation and sanitization
- ✅ Secure authentication and authorization
- ✅ OWASP Top 10 vulnerability prevention
- ✅ Regular security audits and reviews

## 📈 Performance Standards

Optimization guidelines across all modes:

- ✅ Scalability planning for 10x growth
- ✅ Database optimization and indexing
- ✅ Multi-layer caching strategies
- ✅ Load balancing and auto-scaling
- ✅ Resource management and monitoring
- ✅ API performance < 200ms response time

## 🧪 Quality Gates

Each mode enforces specific quality requirements:

- ✅ Files < 500 lines with single responsibility
- ✅ Comprehensive test coverage (>90%)
- ✅ Clean architecture principles applied
- ✅ Proper error handling and logging
- ✅ Security vulnerabilities prevented
- ✅ Documentation updated and accurate

## 🔧 Development Guidelines

### Code Quality Standards

- **DRY Principle**: Eliminate code duplication
- **SOLID Principles**: Follow all five principles consistently
- **Clean Code**: Descriptive naming, minimal nesting
- **Testability**: Design for unit testing with dependency injection
- **Documentation**: Self-documenting code with strategic comments

### Tool Usage Patterns

- Use `apply_diff` for precise code modifications
- Use `insert_content` for new files or empty targets
- Use `write_to_file` for complete file creation
- Always verify parameters before tool execution

## 📊 Agent Categories

### Core Development (39 agents)
- Language specialists (23): Python, JavaScript, TypeScript, Rust, Go, etc.
- Development core (13): Full-stack, frontend, backend specialists
- Special modes (13): Custom workflow modes

### Infrastructure & Operations (28 agents)
- Infrastructure/DevOps (13): Cloud, containers, deployment
- Quality/Security (15): Testing, auditing, compliance specialists

### Business & Analysis (32 agents)
- Business/Product (11): Management, analysis, strategy
- Research/Analysis (9): Data scientists, researchers
- AI/ML specialists (11): Machine learning, computer vision, NLP
- Legal/Compliance (5): Legal advisors, compliance specialists

### Specialized Domains (41 agents)
- Specialized domains (9): FinTech, IoT, blockchain, gaming
- Developer experience (10): Tooling, workflow optimization
- Meta-orchestration (8): Multi-agent coordination
- Additional specialists (14): Various domain experts

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-mode`
3. **Add your custom mode**: Follow the YAML structure in `custom-modes.yaml`
4. **Test thoroughly**: Ensure all quality gates are met
5. **Submit a pull request**: Include detailed description and examples

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Related Projects

- [Roo Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=roocode)
- [Claude Code](https://claude.ai/code)
- [SPARC Methodology](https://github.com/sparc-methodology)

## 📞 Support

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Discussions**: Join community discussions in GitHub Discussions
- **Documentation**: Check the wiki for detailed guides and examples

---

**Total Agents**: 140+ specialist modes
**Last Updated**: 2025-09-20
**Repository**: https://github.com/jtgsystems/Custom-Modes-Roo-Code

✨ *Enhanced AI coding assistance with structured workflows and security-first approach*