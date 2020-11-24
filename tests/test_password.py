import itertools

import pytest

import countersign


@pytest.mark.parametrize('length', [
    1,
    10,
    100,
    1000
])
def test_password_generates_string_of_expected_length(length: int):
    generated_password = countersign.password(length=length)
    assert len(generated_password) == length


@pytest.mark.parametrize('execution_number', range(10))
def test_password_generates_password_only_with_specified_characters(execution_number: int):
    character_pool = '123'
    generated_password = countersign.password(characters=character_pool)
    contains_only_specified_characters = all(character in character_pool for character in generated_password)
    assert contains_only_specified_characters


def test_passwords_generates_expected_number_of_passwords():
    sample_size = 1000
    password_count = len(list(itertools.islice(countersign.passwords(), sample_size)))
    assert password_count == sample_size


def test_passwords_raises_value_error_when_characters_should_be_unique_and_length_is_larger_than_number_of_characters():
    with pytest.raises(ValueError) as exception_info:
        countersign.passwords(characters='123', length=4, unique=True)

    exception = exception_info.value

    actual_message = str(exception)
    expected_message = ('Impossible to build password of all unique characters when the specified length is '
                        'larger than the number of characters specified. Provide a larger collection of characters.')
    assert actual_message == expected_message


@pytest.mark.parametrize('value', [True, False])
def test_passwords_generator_correctly_manages_unique_field(value):
    generator = countersign.PasswordGenerator(characters='123', unique=value, length=1)
    assert generator.unique is value
