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

- **`boomerang-mode`**: A strategic workflow orchestrator that delegates tasks to other specialized modes.
- **`frontend-developer`**: An expert in creating web interfaces using modern frameworks and best practices.
- **`content-strategist`**: Specializes in writing substantial, persuasive, and SEO-aware content.
- **`seo-specialist`**: Focuses on comprehensive on-page and technical SEO optimization.
- **`tool-maker`**: Develops new MCP tools for Roo Code.
- **`mode-creator`**: Defines and creates new custom modes.
- *(... and many others covering various development, business, and creative roles)*

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
    C:\Users\<YourUsername>\AppData\Roaming\Code - Insiders\User\globalStorage\rooveterinaryinc.roo-cline\settings\
    ```
    *(Adjust the path if you use the stable version of VS Code or a different operating system)*.
2.  **Copy Configuration:** Copy the `custom_modes.json` file from this repository into the `settings` directory found in step 1, replacing the existing file if necessary.
3.  **Restart VS Code:** Restart Visual Studio Code to ensure Roo Code loads the new mode definitions.
4.  **Select Mode:** You should now be able to select and use the custom modes defined in this repository within the Roo Code interface.

## 🤝 Contributing

Contributions are welcome! If you improve an existing mode or create a new useful one, feel free to submit a Pull Request. Please ensure:
- The JSON format is valid.
- Instructions are clear and follow the established pattern (including Information Verification and Self-Correction clauses).
- The `botcorrections.json` file is updated if the changes stem from a logged correction.

## 📄 License

*(Optional: Specify a license here if you wish, e.g., MIT License)*
