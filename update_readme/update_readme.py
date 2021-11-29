import os
from csv import DictReader
from datetime import datetime
from jinja2 import Template

FILENAME = "README.md"
README_PATH = os.path.join("../", FILENAME)
TEMPLATE = "templates/README.md.jinja"
FILENAME_CSV = "data/conferences.csv"
DATETIME_FMT = "%Y-%m-%d %H:%M"


def get_datetime():
    """Get datetime.now() in a specific format"""
    _today = datetime.now().strftime(DATETIME_FMT)
    return _today


def build_conf_list(csv_file=FILENAME_CSV, year=None):
    """Parse the csv file, extract and process the data"""
    current_year = datetime.now().year
    all_conferences = list()

    with open(csv_file) as f:
        data = DictReader(f)
        for row in data:
            all_conferences.append(row)

    if year:
        result = [
            conf
            for conf in all_conferences
            if (year in conf["start"] or year in conf["end"])
        ]
    else:
        result = all_conferences

    return result


def write_readme():
    """Write the readme file from a jinja template"""
    with open(TEMPLATE) as f:
        readme_jinja = f.read()

    template = Template(readme_jinja)
    readme_rendered = template.render(last_updated=get_datetime())

    with open(README_PATH, "w") as f:
        f.write(readme_rendered)


if __name__ == "__main__":
    write_readme()
