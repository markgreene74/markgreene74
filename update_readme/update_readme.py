from datetime import datetime

FILENAME = "README.md"


def last_updated():
    _today = datetime.now().strftime("%Y-%m-%d %H:%M")
    return _today


def write_readme():
    _today = last_updated()
    with open(FILENAME, "w") as f:
        f.write(f"Last updated: {_today}")


if __name__ == "__main__":
    write_readme()
