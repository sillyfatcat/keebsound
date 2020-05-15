from pathlib import Path
import pkg_resources
import string
from unittest.mock import call

import pytest

from keeb.main import Keeb


class TestUtils:
    @pytest.fixture
    def setup(self):
        self.sound_profile = 'gateron-red'
        self.keeb = Keeb(self.sound_profile)

    def test_play_single_key(self, mocker, setup):
        alphabet = string.ascii_lowercase
        for letter in alphabet:
            mocked_play_sound = mocker.patch('keeb.main.playsound.playsound')
            self.keeb.play_key(letter)
            mocked_play_sound.assert_has_calls([
                call(Path(pkg_resources.resource_filename('keeb', f'sounds/gateron-red'), f'{letter}.mp3'), block=False),
            ])
            assert 1 == mocked_play_sound.call_count

    def test_play_single_combination_key(self, mocker, setup):
        alphabet = string.ascii_uppercase
        for letter in alphabet:
            mocked_play_sound = mocker.patch('keeb.main.playsound.playsound')
            self.keeb.play_key(letter)
            mocked_play_sound.assert_has_calls([
                call(Path(pkg_resources.resource_filename('keeb', f'sounds/gateron-red'), 'LSHIFT.mp3'), block=False),
                call(Path(pkg_resources.resource_filename('keeb', f'sounds/gateron-red'), f'{letter.lower()}.mp3'), block=False),
            ])
            assert 2 == mocked_play_sound.call_count
