import os
from csv import DictReader
from datetime import datetime as dt
from jinja2 import Template

FILENAME = "README.md"
README_PATH = os.path.join("../", FILENAME)
TEMPLATE = "templates/README.md.jinja"
FILENAME_CSV = "data/conferences.csv"
DATETIME_FMT = "%Y-%m-%d %H:%M"


def get_datetime():
    """Get datetime.now() in a specific format"""
    _today = dt.now().strftime(DATETIME_FMT)
    return _today


def build_conf_list(csv_file=FILENAME_CSV, year=None):
    """Parse the csv file, extract and process the data"""
    with open(csv_file) as f:
        data = DictReader(f)
        all_conferences = [row for row in data]
    # "conference","start","end","online","fee","registered","attended","website"

    # process the data
    for conf in all_conferences:
        # replace "True"/"False" with a boolean
        for k in ["online", "fee", "registered", "attended"]:
            conf[k] = True if conf[k].lower() == "true" else False
        # replace str with a proper datetime.date object,
        # if it's a one day conference set start date to None
        conf["start"] = (
            None
            if conf["start"] == conf["end"]
            else dt.strptime(conf["start"], "%d/%m/%Y").date()
        )
        conf["end"] = dt.strptime(conf["end"], "%d/%m/%Y").date()
        # add a key/value with the n of days, set to 1 for one-day conferences
        conf["days"] = (conf["end"] - conf["start"]).days + 1 if conf["start"] else 1

    # now we can order the conferences, for example by end date
    all_conferences.sort(key=lambda x: x["end"], reverse=False)

    # decide what to return based on if the arg `year` was provided
    if year:
        y = int(year)
        conf_new = [conf for conf in all_conferences if conf["end"].year >= y]
        conf_old = [conf for conf in all_conferences if conf["end"].year < y]
    else:
        conf_new = all_conferences
        conf_old = []

    return conf_new, conf_old


def write_readme():
    """Write the readme file from a jinja template"""
    with open(TEMPLATE) as f:
        readme_jinja = f.read()

    current_year = dt.now().year
    conf_new, conf_old = build_conf_list(year=current_year)

    template = Template(readme_jinja)
    readme_rendered = template.render(
        last_updated=get_datetime(),
        current_year=current_year,
        conf_new=conf_new,
        conf_old=conf_old,
    )

    with open(README_PATH, "w") as f:
        f.write(readme_rendered)


if __name__ == "__main__":
    write_readme()
