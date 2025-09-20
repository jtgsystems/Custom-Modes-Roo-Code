# Roo Code Custom Modes Setup Guide

## Installation

1. **Install Roo Code Extension**
   ```bash
   # Install from VS Code Marketplace
   # Search for "Roo Code" and install
   ```

2. **Clone This Repository**
   ```bash
   git clone https://github.com/jtgsystems/Custom-Modes-Roo-Code.git
   cd Custom-Modes-Roo-Code
   ```

3. **Configure Roo Code**
   - Open VS Code settings
   - Navigate to Roo Code settings
   - Point to `roo-modes.yaml` for custom modes

## Quick Start

1. **Open Command Palette** (`Cmd/Ctrl + Shift + P`)
2. **Select "Roo: Switch Mode"**
3. **Choose from available modes:**
   - 🏗️ System Architect - For architecture design
   - 🚀 Full-Stack Engineer - For complete feature development
   - 🔒 Security Engineer - For security implementation
   - ⚙️ DevOps Engineer - For infrastructure and deployment
   - 🤖 AI Engineer - For AI/ML integration

## Configuration

### Workspace Settings
Create `.vscode/settings.json` in your project:
```json
{
  "roo.customModes": "./roo-modes.yaml",
  "roo.enableAGENTS": true,
  "roo.agentsFile": "./AGENTS.md"
}
```

### Project-Specific Rules
Add `AGENTS.md` to your project root with specific guidelines.

## 2025 Features

- **Agent Rules Standard**: Unified guidelines via AGENTS.md
- **Multi-Agent Coordination**: Multiple specialists working together
- **Security-First**: Built-in security scanning and compliance
- **Performance Optimized**: Sub-200ms response time targets
- **Type-Safe**: End-to-end TypeScript integration

## Troubleshooting

### Common Issues
1. **Modes Not Loading**: Check YAML syntax in `roo-modes.yaml`
2. **Permission Errors**: Ensure read access to configuration files
3. **Performance Issues**: Reduce context size or enable caching

### Support
- GitHub Issues: Report bugs and feature requests
- Documentation: Check `/docs` for detailed guides
- Examples: See `/examples` for usage patterns