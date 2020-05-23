import itertools
import re
import string
from re import Pattern
from typing import Sequence, Generator

import pytest

from countersign.passphrase import OneTimePasswordGenerator, DigitGenerationStrategy, DigitPlacementStrategy, \
    passphrase, passphrases


@pytest.fixture
def test_words() -> Sequence[str]:
    return ['test', 'words']


def test_one_time_password_generator_generates_only_one_unique_string():
    sample_size = 1000
    generator = OneTimePasswordGenerator(characters=string.ascii_letters, length=8, unique=False)
    generated = list(itertools.islice(next(generator), sample_size))
    assert len(generated) == sample_size

    generated_without_duplicates = set(generated)
    assert len(generated_without_duplicates) == 1


def test_generator_constructed_from_non_unique_digit_generation_strategy_should_behave_correctly():
    sample_size = 1000
    generator = DigitGenerationStrategy(3, placement=DigitPlacementStrategy.AFTER, unique=False).to_digit_generator()
    generated = list(itertools.islice(generator, sample_size))
    assert len(generated) == sample_size

    generated_without_duplicates = set(generated)
    assert len(generated_without_duplicates) == 1


def test_generator_constructed_from_unique_digit_generation_strategy_should_behave_correctly():
    sample_size = 100
    generator = DigitGenerationStrategy(10, placement=DigitPlacementStrategy.AFTER).to_digit_generator()
    generated = list(itertools.islice(generator, sample_size))
    assert len(generated) == sample_size

    generated_without_duplicates = set(generated)
    assert len(generated_without_duplicates) == sample_size


# TODO: Clean unit test up
@pytest.mark.parametrize('word_count,digit_count,placement_strategy,pattern', [
    (2, 3, DigitPlacementStrategy.BEFORE, re.compile(r'^\d{3}[a-z]+$')),
    (2, 3, DigitPlacementStrategy.AFTER, re.compile(r'^[a-z]+\d{3}$')),
    (2, 3, DigitPlacementStrategy.BEFORE_AND_AFTER, re.compile(r'^\d{3}[a-z]+\d{3}$')),
    (2, 3, DigitPlacementStrategy.IN_BETWEEN, re.compile(r'^[a-z]+\d{3}[a-z]+$')),
    (2, 3, DigitPlacementStrategy.AROUND, re.compile(r'^\d{3}[a-z]+\d{3}[a-z]+\d{3}$'))
])
def test_passphrase_correctly_places_digits(test_words: Sequence[str],
                                            word_count: int,
                                            digit_count: int,
                                            placement_strategy: DigitPlacementStrategy,
                                            pattern: Pattern):
    digit_strategy = DigitGenerationStrategy(digit_count=digit_count,
                                             placement=placement_strategy,
                                             unique=False)
    generated_passphrase = passphrase(test_words, word_count=word_count, digit_strategy=digit_strategy)

    assert pattern.match(generated_passphrase) is not None


def test_passphrase_does_not_place_digits_when_strategy_is_not_provided(test_words):
    generated_passphrase = passphrase(test_words)
    pattern = re.compile(r'^\w+$')

    assert pattern.match(generated_passphrase) is not None


def test_passphrases_correctly_produces_passphrase_generator(test_words):
    passphrase_generator = passphrases(test_words)

    assert isinstance(passphrase_generator, Generator)
