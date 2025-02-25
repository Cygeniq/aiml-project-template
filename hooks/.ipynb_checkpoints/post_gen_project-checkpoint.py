#!/usr/bin/env python
import os
import shutil
from pathlib import Path

def main():
    """
    Post-project generation hook to customize the generated project
    based on user selections.
    """
    print("Debug: include_notebooks value is '{{ cookiecutter.include_notebooks }}'")
    
    # Get the current directory (project root)
    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
    
    # Create directories not tracked by git
    create_directories = [
        os.path.join("data", "raw"),
        os.path.join("data", "processed"),
        os.path.join("data", "interim"),
        os.path.join("models"),
        os.path.join("docs", "tasks")
    ]
    
    for directory in create_directories:
        os.makedirs(os.path.join(PROJECT_DIRECTORY, directory), exist_ok=True)
        # Create .gitkeep files to track empty directories
        with open(os.path.join(PROJECT_DIRECTORY, directory, ".gitkeep"), "w") as f:
            pass
    
    # Create notebooks directory if required
    print(f"Debug: Checking if '{{ cookiecutter.include_notebooks }}' equals 'true' or 'y'")
    
    if '{{ cookiecutter.include_notebooks }}'.lower().strip() in ['true', 'y', 'yes']:
        print("Debug: Creating notebooks directories")
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "notebooks", "exploration"), exist_ok=True)
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "notebooks", "modeling"), exist_ok=True)
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "notebooks", "evaluation"), exist_ok=True)
        # Add .gitkeep files
        for subdir in ["exploration", "modeling", "evaluation"]:
            with open(os.path.join(PROJECT_DIRECTORY, "notebooks", subdir, ".gitkeep"), "w") as f:
                pass
    else:
        # Remove notebooks directory if it exists
        if os.path.exists(os.path.join(PROJECT_DIRECTORY, "notebooks")):
            shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "notebooks"))
    
        # Remove tests directory if not required
    if '{{ cookiecutter.include_tests }}' != 'true':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "tests"))
    
    # Remove docs directory if not required
    if '{{ cookiecutter.include_docs }}' != 'true':
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "docs"))
    
    # Set up project-specific directories based on project type
    project_type = '{{ cookiecutter.project_type }}'
    
    if project_type == 'nlp':
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "src", "nlp"), exist_ok=True)
        # Create NLP-specific files
        with open(os.path.join(PROJECT_DIRECTORY, "src", "nlp", "__init__.py"), "w") as f:
            pass
        with open(os.path.join(PROJECT_DIRECTORY, "src", "nlp", "text_processor.py"), "w") as f:
            f.write("# Text processing utilities\n")
    
    if project_type == 'genai':
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "src", "llm"), exist_ok=True)
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "src", "rag"), exist_ok=True)
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "src", "vector_store"), exist_ok=True)
        
        # Create GenAI-specific files
        with open(os.path.join(PROJECT_DIRECTORY, "src", "llm", "__init__.py"), "w") as f:
            pass
        with open(os.path.join(PROJECT_DIRECTORY, "src", "rag", "__init__.py"), "w") as f:
            pass
        with open(os.path.join(PROJECT_DIRECTORY, "src", "vector_store", "__init__.py"), "w") as f:
            pass
    
    if project_type == 'computer_vision':
        os.makedirs(os.path.join(PROJECT_DIRECTORY, "src", "vision"), exist_ok=True)
        # Create CV-specific files
        with open(os.path.join(PROJECT_DIRECTORY, "src", "vision", "__init__.py"), "w") as f:
            pass
        with open(os.path.join(PROJECT_DIRECTORY, "src", "vision", "image_processor.py"), "w") as f:
            f.write("# Image processing utilities\n")
    
    # Create an initial .gitignore file
    gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
dist/
build/
*.egg-info/

# Unit test / coverage reports
htmlcov/
.coverage
.coverage.*
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints

# Environments
.env
.venv
env/
venv/
ENV/

# VS Code
.vscode/

# PyCharm
.idea/

# Data
data/raw/*
!data/raw/.gitkeep
data/processed/*
!data/processed/.gitkeep
data/interim/*
!data/interim/.gitkeep

# Models
models/*
!models/.gitkeep

# Logs
logs/
*.log
"""
    
    with open(os.path.join(PROJECT_DIRECTORY, ".gitignore"), "w") as f:
        f.write(gitignore_content)
    
    # Create a minimal setup.py file
    setup_py_content = """
from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.1.0',
    description='{{ cookiecutter.project_description }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'pyyaml',
    ],
    extras_require={
        'dev': [
            'pytest',
            'black',
            'flake8',
            'jupyter',
        ],
    },
)
"""
    
    with open(os.path.join(PROJECT_DIRECTORY, "setup.py"), "w") as f:
        f.write(setup_py_content)
    
    print("Project successfully created!")
    print("\nNext steps:")
    print("1. Create and activate a virtual environment")
    print("2. Install dependencies: 'make requirements'")
    print("3. Initialize git repository")
    print("4. Start coding!\n")

if __name__ == '__main__':
    main()
