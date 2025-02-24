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
