# Security77

A command line tool and python package to make security simple. Command `s77`

# Features

- Generate password;

# ToDo/Ideas

- [ ] Generate Django Secret Key;
- [ ] Generate password;
- [ ] Validate password force;
- [ ] Generate Custom Wordlist with data from user (name, age, animal, family, religion, ...);
- [ ] Scan home directory to get passwords;
- [ ] Get WiFi password;

# Install

Requirements

- Python

## How to install?

```bash
pip install security77
``` 

# Usage

Some examples of usage.

### Generate Django Secret Key

```bash
s77 django-secret-key-gen
``` 

### Generate Password

```bash
s77 passgen --size=16 --charlist=[all|numbers|letters|numbers_letters|low_letters|up_letters|special_chars] --custom-charlist=abc123
```

# Tests

Run local tests (development).

```bash
make test
``` 

# License

MIT LICENSE (c) 2021 Wallace Silva
