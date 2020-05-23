import itertools

from countersign.core import StringGenerator


class DummyStringGenerator(StringGenerator):
    """
    Dummy string generator implementation for testing
    """

    def generate(self) -> str:
        return 'dummy'


def test_string_generator_is_iterable():
    generator = DummyStringGenerator()
    sample_size = 10
    generated_strings = list(itertools.islice((generation for generation in generator), sample_size))

    assert len(generated_strings) == sample_size
