# Data and AI Project Template
  Powered by Visual Studio Code
  Author: Dr. Shadi Saleh
  Date: July 2025

## Cookiecutter Data Science
This project template is a simplified version 

## Essential Setup
 Installation: IDE: Visual Studio Code
    Download: https://code.visualstudio.com/
### Python & Conda
    Install Python: https://www.python.org/downloads/
    [OR] Recommended: Install Miniconda or Anaconda for environment and package management
    Miniconda : https://www.anaconda.com/docs/getting-started/miniconda/install
    Conda : https://www.anaconda.com/download

## 🔌Recommended Extensions:
| Extension Name      | Purpose                                     |
| ------------------- | ------------------------------------------- |
| Python              | Syntax, linting, environment management     |
| Jupyter             | Notebook editing and execution              |
| Pylance             | Fast IntelliSense and type checking         |
| GitLens             | Git history, blame, and insights            |
| Docker              | Manage containers and images inside VS Code |
| Remote - Containers | Dev inside Docker-based environments        |
| Jupyter Keymap      | Familiar keybindings in notebooks           |
| Black Formatter     | Automatic code formatting                   |


## Adjusting .gitignore

Ensure you adjust the `.gitignore` file according to your project needs. For example, since this is a template, the `/data/` folder is commented out and data will not be exlucded from source control:

```plaintext
# exclude data from source control by default
# /data/
```

Typically, you want to exclude this folder if it contains either sensitive data that you do not want to add to version control or large files.

## 🔒 Environment Variables Setup: Duplicating the .env File

To set up your environment variables, you need to duplicate the `.env.example` file and rename it to `.env`. You can do this manually or using the following terminal command:

```bash
cp .env.example .env # Linux, macOS, Git Bash, WSL
copy .env.example .env # Windows Command Prompt
```

This command creates a copy of `.env.example` and names it `.env`, allowing you to configure your environment variables specific to your setup.
Use the .env file to securely manage API keys, database URIs, or experiment config settings.

## 🚫 Version Control & .gitignore Setup
    # Ignore data by default
    # /data/

    # Common ignores
    __pycache__/
    *.pyc
    .env
    .ipynb_checkpoints/
    models/



## Project Directory Structure (Project Organization)

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── src                         <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    │    
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    ├── plots.py                <- Code to create visualizations 
    │
    └── services                <- Service classes to connect with external platforms, tools, or APIs
        └── __init__.py 
```

## ⚙️ Environment Setup
   ✅ Create Conda Environment
        conda create -n data-ai python=3.10 -y
        conda activate data-ai
  ✅ Install Dependencies:
      Install Essential Libraries via pip
        pip install numpy pandas matplotlib seaborn scikit-learn jupyter notebook
        pip install xgboost lightgbm
        pip install jupyterlab ipywidgets
        pip install black flake8 isort
        
        #pip install tensorflow torch torchvision # Note: Further configuration may be required depending on whether you intend to run on GPU or CPU # (Can be ignored here for basic usage or testing.)

    Or 
        pip install -r requirements.txt
    or export your environment:
        pip freeze > requirements.txt


## 🐳 Docker Support
    Add a Dockerfile and .devcontainer/ setup if you want full containerized reproducibility.
    Example extensions to support Docker workflows in VS Code:
        - Docker: View/manage containers and images
        - Remote - Containers: Work in a containerized dev environment
        - Dev Containers CLI: Automate container setup from .devcontainer.json

## ➕ Optional Sections to Improve This Template
| Section                 | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| **Testing**             | Add a `tests/` folder with `pytest` or `unittest` for modular testing    |
| **Data Validation**     | Integrate tools like `pandera` or `great_expectations`                   |
| **CI/CD**               | Add GitHub Actions or GitLab pipelines for automated testing and linting |
| **Experiment Tracking** | Integrate `MLflow` or `Weights & Biases` to track training runs          |
| **Docker Deployment**   | Add Dockerfile and Docker Compose for deployment                         |
| **Makefile**            | Add useful automation commands (`make train`, `make test`, etc.)         |
| **Pre-commit Hooks**    | Ensure code quality using `pre-commit` for linting/formatting            |




--------
