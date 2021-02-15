import pytest

from freezegun import freeze_time
from datetime import datetime

import update_readme as updt

def test_add_last_updated():
    _mock_date = "2021-01-01T00:00:00"
    with freeze_time(_mock_date):
        print(datetime.now())
        assert datetime.isoformat(updt.add_last_updated()) == _mock_date
