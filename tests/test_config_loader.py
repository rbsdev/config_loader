import pytest
from nose.tools import raises

from src.config_loader import ConfigLoader


class TestExample(object):

    def test_(self):
        c = ConfigLoader()
        assert c.load_config_from_file('dev'), "This should not fail"

    @pytest.mark.xfail
    @raises(IOError)
    def test_failing(self):
        c = ConfigLoader()
        assert c.load_config_from_file('hlg'), "This will always fail"
