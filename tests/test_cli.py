from unittest.mock import call

from click.testing import CliRunner
from keeb.main import main
import pytest


class TestCLI:
    @pytest.fixture
    def setup(self):
        self.runner = CliRunner()

    def test_hook(self, mocker, setup):
        mocked_hook = mocker.patch('keeb.main.Keeb.hook_keyboard')
        result = self.runner.invoke(main, ['--hook'])
        assert 0 == result.exit_code
        mocked_hook.assert_called_once()

    def test_no_params(self, setup):
        result = self.runner.invoke(main, [])
        assert 1 == result.exit_code

    def test_cli_play_string(self, mocker, setup):
        mocked_play_string = mocker.patch('keeb.main.Keeb.play_string')
        result = self.runner.invoke(main, ['--string', 'foo bar'])
        assert 0 == result.exit_code
        mocked_play_string.assert_called_with('foo bar')

    def test_play_string(self, mocker, setup):
        mocker.patch('keeb.main.sleep')
        mocked_play_sound = mocker.patch('keeb.main.playsound.playsound')
        string = 'foo bar'
        result = self.runner.invoke(main, ['--string', string])
        assert 0 == result.exit_code
        assert len(string) == mocked_play_sound.call_count
