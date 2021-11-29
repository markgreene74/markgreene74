from datetime import datetime
from jinja2 import Template
import os

FILENAME = "README.md"
README_PATH = os.path.join("../", FILENAME)
TEMPLATE = "templates/README.md.jinja"
DATETIME_FMT = "%Y-%m-%d %H:%M"


def get_datetime():
    """Get datetime.now() in a specific format"""
    _today = datetime.now().strftime(DATETIME_FMT)
    return _today


def build_conf_list():
    pass


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
