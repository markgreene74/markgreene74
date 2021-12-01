import pytest

import os
from shutil import copytree
from csv import DictReader
from datetime import datetime as dt
from freezegun import freeze_time

import update_readme as updt

FILENAME = "README.md"
README_PATH = os.path.join("../", FILENAME)
TEMPLATE = "templates/README.md.jinja"
FILENAME_CSV = "test/test_data.csv"
DATETIME_FMT = "%Y-%m-%d %H:%M"
TEMPLATE_DIR = "templates"


def test_get_datetime():
    _mock_date = "2021-01-01 00:00"
    with freeze_time(_mock_date):
        assert updt.get_datetime() == _mock_date


def test_conference_year():
    _year = "2021"
    _new, _old = updt.build_conf_list(FILENAME_CSV, _year)
    assert len(_new) == 2
    assert len(_old) == 3


def test_build_conf_list():
    _new, _old = updt.build_conf_list(FILENAME_CSV)
    assert len(_new) == 5
    assert len(_old) == 0


def test_readme(tmp_path):
    base_dir = os.path.join(tmp_path, "update_readme")
    os.mkdir(base_dir)
    copytree(TEMPLATE_DIR, os.path.join(base_dir, TEMPLATE_DIR))
    os.chdir(base_dir)

    updt.write_readme()
    _today = dt.now().strftime(DATETIME_FMT)

    with open(README_PATH) as temp_file:
        readme_file = temp_file.read()

    assert f"Last updated: {_today}" in readme_file
