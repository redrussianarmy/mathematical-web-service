""" Python Unit Test Coverage Script """

import os
import pathlib
from helpers import set_python_path

PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve()

if __name__ == '__main__':
    app_path = os.path.join(PROJECT_ROOT, "web_service")
    run_ut = "algorithms.tests"

    set_python_path()

    commands = [
        f"coverage run --source={app_path} {app_path}\\manage.py test {run_ut}",
        f"coverage report --omit=algorithms.tests\*",
        f"coverage html --omit=*urls*,*__init__*,*scripts*,*manage*,*base*,*admin*,*tests*,*apps* -d coverage-report"
    ]

    rett_code = 0
    for command in commands:
        rett_code = os.system(command)
        if rett_code != 0:
            exit(1)
    exit(rett_code)
