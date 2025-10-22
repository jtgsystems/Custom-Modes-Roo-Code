# Contributing to Custom Modes for Roo Code 🤝

First off, thank you for considering contributing to Custom Modes for Roo Code! It's people like you that make this project a great tool for developers worldwide.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Agent Submission Guidelines](#agent-submission-guidelines)
- [Development Workflow](#development-workflow)
- [Style Guide](#style-guide)
- [Commit Messages](#commit-messages)

## 📜 Code of Conduct

This project and everyone participating in it is governed by respect, professionalism, and collaboration. By participating, you are expected to uphold this standard.

## 🎯 How Can I Contribute?

### Reporting Bugs 🐛

Before creating bug reports, please check existing issues. When you create a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Roo Code version, etc.)

### Suggesting Enhancements ✨

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear use case** description
- **Detailed explanation** of the proposed functionality
- **Examples** of similar implementations if available

### Adding New Agents 🤖

We welcome new agent contributions! See the [Agent Submission Guidelines](#agent-submission-guidelines) below.

## 📝 Agent Submission Guidelines

### Agent Requirements

All new agents must:

1. **Follow the standard YAML structure**
2. **Include comprehensive role descriptions**
3. **Specify security features** (2025 standards)
4. **List relevant frameworks and capabilities**
5. **Be tested** with Roo Code CLI
6. **Include practical examples**

### Agent Structure Template

```yaml
name: "Agent Name"
version: "2025.1"
category: "category-name"
subcategory: "subcategory-name"
description: "Brief one-line description"

role: |
  Detailed multi-line role description.
  Explain what this agent does and when to use it.

capabilities:
  - Capability 1
  - Capability 2
  - Capability 3

frameworks:
  - Framework 1
  - Framework 2

security_features:
  - input_validation
  - secure_coding_practices
  - vulnerability_scanning

best_practices:
  - Practice 1
  - Practice 2

examples:
  - example: "Use case 1"
    command: "roo-code command"
  - example: "Use case 2"
    command: "roo-code command"
```

### Agent Categories

Place your agent in the appropriate directory:

- `agents/ai-ml/` - AI and Machine Learning
- `agents/business-product/` - Business and Product Management
- `agents/core-development/` - Core Development Roles
- `agents/infrastructure-devops/` - Infrastructure and DevOps
- `agents/language-specialists/` - Programming Language Experts
- `agents/legal-compliance/` - Legal and Compliance
- `agents/meta-orchestration/` - System Orchestration
- `agents/security-quality/` - Security and Quality Assurance
- `agents/specialized-domains/` - Industry-Specific Expertise

## 🔄 Development Workflow

### 1. Fork the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Custom-Modes-Roo-Code.git
cd Custom-Modes-Roo-Code
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/new-agent-name
# or
git checkout -b fix/issue-description
```

### 3. Make Your Changes

- Add your agent YAML file to the appropriate directory
- Update the main `custom_modes.yaml` if needed
- Test your agent with Roo Code CLI

### 4. Validate Your Agent

```bash
# Run validation script
python3 scripts/validate_custom_modes.py agents/category/your-agent.yaml

# Test with Roo Code
roo-code validate agents/category/your-agent.yaml
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add Python FastAPI expert agent"
```

### 6. Push to Your Fork

```bash
git push origin feature/new-agent-name
```

### 7. Create a Pull Request

- Go to the [repository on GitHub](https://github.com/jtgsystems/Custom-Modes-Roo-Code)
- Click "New Pull Request"
- Select your fork and branch
- Fill out the PR template

## 🎨 Style Guide

### YAML Formatting

- Use **2 spaces** for indentation (no tabs)
- Keep lines under **100 characters** when possible
- Use **lowercase** with hyphens for file names (`python-developer.yaml`)
- Add **blank line** between major sections

### Documentation

- Use **clear, concise language**
- Include **code examples** where appropriate
- Add **comments** for complex configurations
- Keep **README** up to date

## ✍️ Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature or agent
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes (no code change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(agents): add Rust systems programming agent

- Added comprehensive Rust developer agent
- Includes async/await patterns
- WebAssembly support
- Memory safety best practices

Closes #42
```

```bash
fix(validation): correct YAML schema validation

- Fixed schema validation for nested capabilities
- Added error handling for missing fields

Fixes #38
```

## 🧪 Testing

Before submitting:

1. **Validate YAML syntax**
   ```bash
   python3 scripts/validate_custom_modes.py your-agent.yaml
   ```

2. **Test with Roo Code CLI**
   ```bash
   roo-code test agents/category/your-agent.yaml
   ```

3. **Check for security issues**
   - Ensure all security features are documented
   - Follow 2025 security standards

## 📊 Pull Request Checklist

Before submitting your PR, ensure:

- [ ] Agent follows the standard YAML structure
- [ ] Agent is placed in the correct category directory
- [ ] Agent includes comprehensive role description
- [ ] Security features are documented
- [ ] Agent has been tested with Roo Code CLI
- [ ] YAML syntax is valid
- [ ] Documentation is updated if needed
- [ ] Commit messages follow conventional commits format
- [ ] No merge conflicts with main branch

## 🚀 After Your PR is Merged

- Your agent will be included in the next release
- You'll be added to the contributors list
- Your agent will be available to all Roo Code users

## 📞 Questions?

If you have questions:

- 💬 Open a [GitHub Discussion](https://github.com/jtgsystems/Custom-Modes-Roo-Code/discussions)
- 🐛 Create an [Issue](https://github.com/jtgsystems/Custom-Modes-Roo-Code/issues)
- 📧 Email: support@jtgsystems.com

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

---

**Happy Contributing!** 🎉

[![Built with ❤️ by JTG Systems](https://img.shields.io/badge/Built%20with-%E2%9D%A4%EF%B8%8F-red)](https://github.com/jtgsystems)
