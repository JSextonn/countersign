# Countersign
![](https://github.com/jsextonn/countersign/workflows/build/badge.svg)

`countersign - A signal or password given in reply to a soldier on guard.`

Countersign is a light-weight python library for generating highly customizable passwords. 

## Installation

`pip install countersign`

## Usage

### Passwords
In countersign terms passwords are simply random character strings that are slightly configurable.

To generate a random password, import the `password()` function.

```python
from countersign.password import password

# By default, generates some random password using 'string.printable' characters of length 8
generated_password = password()
```

Configuration can be accomplished as seen below.

```python
from countersign.password import password

# Generates password of all unique characters using
# the characters '12345' with a length of 2
generated_password = password(characters='12345', length=2, unique=True)
```

If you require multiple random passwords to be generated at a time, use the `passwords()` function. The function returns a python generator that yields an unlimited count of random passwords and can bee configured the same as the `password()` function.

```python
from countersign.password import passwords

# Returns a python generator capable of producing passwords with default characteristics
password_generator = passwords()
```

### Passphrases
Passphrases are more structured passwords following certain configured patterns and even using given world dictionaries. Completely random passwords are great but sometimes a more human memorable pattern is more ideal.

Similar to passwords, passphrases can be constructed and configured the same way.

```python
from countersign.passphrase import passphrase

words = ['Test', 'Word', 'More', 'Words']

# Passphrase using the words [Test, Word, More, Words] with no digit generation strategy. By default the passphrase consists of three given words.
# Produces something like: WordMoreTest
generated_passphrase = passphrase(words)
```

Passphrases can also be configured with a digit generation strategy which tells the passphrase generator to inject digit groups wherever specified.

```python
from countersign.passphrase import passphrase, DigitGenerationStrategy, DigitPlacementStrategy

words = ['Test', 'Word', 'More', 'Words']

strategy = DigitGenerationStrategy(digit_count=3, placement=DigitPlacementStrategy.AFTER)

# Produces something like: WordWordsTest947
generated_passphrase = passphrase(words, digit_strategy=strategy)
```

Digit placement strategies include:
- BEFORE `123TestWords`

- AFTER `TestWords123`

- BEFORE_AND_AFTER `123TestWords123`

- IN_BETWEEN `Test123Words`

- AROUND `123Test123Words123`


