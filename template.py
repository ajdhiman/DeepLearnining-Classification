import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

projectName = "DeepLearningClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/configs/__init__.py",
    f"src/{projectName}/pipelines/__init__.py",
    f"src/{projectName}/entities/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    f"src/{projectName}/__init__.py",
    "configs/congig.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.config",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipnyb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    fileDir, fileName = os.path.split(filepath)
    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory: {fileDir} for file: {fileName}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{fileName} already exists")