""" Python Environment Preparation Script """

import os
import platform
import subprocess
import pathlib
from helpers import set_python_path


PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()
OS_TYPE = platform.system()


def get_venv():
    venv = os.path.join(PROJECT_ROOT, "env")
    if OS_TYPE == "Windows":
        venv_python = os.path.join(venv, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(venv, "bin", "python.exe")
    return venv, venv_python


def upgrade_pip():
    subprocess.call(
        ["python", "-m", "pip", "install", "--upgrade", "pip"]
    )


def pip_install(package=None, file_path=None):
    def arg(): return [package] if package else ['-r', file_path]
    install_req = subprocess.call(
        ["pip", "install", *arg()]
    )
    return install_req


def create_virtualenv():
    venv, venv_python = get_venv()
    pip_install(package="virtualenv")

    if not os.path.exists(venv_python):
        print("Environment is being creating...")
        subprocess.call(["python", "-m", "virtualenv", venv])
    else:
        print("Environment already exists: ", venv_python)
        print("Checking for updates")


def install_requirements():
    requirements_path = os.path.join(PROJECT_ROOT, "requirements.txt")
    result = pip_install(file_path=requirements_path)

    return result


if __name__ == "__main__":
    venv, _ = get_venv()
    create_virtualenv()
    set_python_path()
    upgrade_pip()
    installation_result = install_requirements()
    exit(installation_result)
