# Template Usage Guide

This document provides instructions on how to use the AI/ML project template to standardize development workflow across your team.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip
- cookiecutter (`pip install cookiecutter`)

### Setting Up the Template

1. **Make the template available to your team**

   Option A: Host on internal Git repository:
   ```bash
   git clone https://github.com/your-org/aiml-project-template.git
   cd aiml-project-template
   git push <your-internal-git-url>
   ```

   Option B: Share locally:
   ```bash
   # Copy to a shared network location
   cp -r aiml-project-template /path/to/shared/location/
   ```

2. **Install cookiecutter (if not already installed)**
   ```bash
   pip install cookiecutter
   ```

## Creating a New Project

### Basic Usage

1. **Create a new project from the template**
   ```bash
   # From a git repository
   cookiecutter git@your-internal-git:your-org/aiml-project-template.git
   
   # From a local directory
   cookiecutter /path/to/shared/location/aiml-project-template
   ```

2. **Follow the prompts to configure your project**
   - Enter project name
   - Select project type
   - Enter JIRA ticket number
   - Configure other options

3. **Initialize git repository**
   ```bash
   cd your_new_project
   git init
   git add .
   git commit -m "Initial commit from template"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

### Workflow for New Tasks

1. **Create a new branch for your task**
   ```bash
   git checkout -b feature/JIRA-XXX-description
   ```

2. **Create task documentation**
   ```bash
   make new-task
   # Enter JIRA ticket number when prompted
   # Enter task title when prompted
   ```

3. **Implement your task following the structure**
   - Add data processing code in `src/data/`
   - Add model code in `src/models/`
   - Add evaluation code in `src/evaluation/`
   - Add utility functions in `src/utils/`

4. **Run tests to ensure quality**
   ```bash
   make test
   ```

5. **Format your code**
   ```bash
   make format
   ```

6. **Submit your work**
   ```bash
   git add .
   git commit -m "JIRA-XXX: Implement feature"
   git push origin feature/JIRA-XXX-description
   # Create a pull request
   ```

## Template Structure

The template provides a standardized structure that works well for most AI/ML projects:

- **src/**: Main source code
  - **data/**: Data loading and processing
  - **features/**: Feature engineering
  - **models/**: Model definition, training, and inference
  - **evaluation/**: Metrics and evaluation tools
  - **utils/**: Utility functions

- **notebooks/**: Jupyter notebooks for exploration and demonstration
  - Contains template notebooks for common tasks

- **tests/**: Automated tests
  - Unit tests for components
  - Integration tests

- **configs/**: Configuration files
  - YAML files for experiment settings

- **docs/**: Documentation
  - Documentation for the project
  - Task templates for standardized task tracking

## Extending the Template

You can customize the template for your team's specific needs:

1. **Add specialized components for your domain**
   - Add additional directories or files
   - Modify the cookiecutter.json to include more options

2. **Add team-specific scripts**
   - Extend the Makefile with custom commands
   - Add deployment scripts

3. **Update documentation templates**
   - Customize the task template
   - Add organization-specific guidelines

## Best Practices

1. **Document each task**
   - Use the task template for consistency
   - Include requirements and acceptance criteria

2. **Use the Makefile**
   - Common tasks are standardized with make commands
   - Add new commands as needed

3. **Follow the structure**
   - Keep code organized according to the template
   - Don't fight the structure; extend it if needed

4. **Version control**
   - Commit early and often
   - Use descriptive commit messages with JIRA references

5. **Testing**
   - Write tests for new functionality
   - Run tests before submitting code

## Common Issues and Solutions

**Problem**: Template doesn't include specialized libraries for my task.

**Solution**: Add them to the `requirements.txt` file or modify the template's default requirements.

---

**Problem**: The structure doesn't fit my specific workflow.

**Solution**: Extend the structure by adding directories or modifying the template. Document these changes for your team.

---

**Problem**: I need to add team-specific conventions.

**Solution**: Modify the template or add documentation in your team's wiki, linking to this guide. 
