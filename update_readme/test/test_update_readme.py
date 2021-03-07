import pytest
import os
from shutil import copytree

from freezegun import freeze_time
from datetime import datetime

import update_readme as updt

FILENAME = "README.md"
TEMPLATE = "templates/README.md.jinja"
TEMPLATE_DIR = "templates"
DATETIME_FMT = "%Y-%m-%d %H:%M"


def test_get_datetime():
    _mock_date = "2021-01-01 00:00"
    with freeze_time(_mock_date):
        assert updt.get_datetime() == _mock_date


def test_readme(tmp_path):
    copytree(TEMPLATE_DIR, os.path.join(tmp_path, TEMPLATE_DIR))
    os.chdir(tmp_path)

    updt.write_readme()
    _today = datetime.now().strftime(DATETIME_FMT)

    with open(FILENAME) as temp_file:
        readme_file = temp_file.read()

    assert f"Last updated: {_today}" in readme_file
