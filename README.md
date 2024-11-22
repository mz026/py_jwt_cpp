[![Unit Tests](https://github.com/mz026/py_jwt_cpp/actions/workflows/unit_test.yml/badge.svg)](https://github.com/mz026/py_jwt_cpp/actions/workflows/unit_test.yml)

# py_jwt_cpp

A Python wrapper around [jwt-cpp](https://github.com/Thalhammer/jwt-cpp).


## Installation

`pip install py_jwt_cpp`

## Usage

```python
import py_jwt_cpp

jwt = py_jwt_cpp.encode(
    data={'key': 'val'},
    private_key='*****',
    headers={'kid': 'value'}
)
```

where:

- `data`: A `dict` with string key and string value.
- `private_key`: string, an RS256-compatible private key.
- `headers`: [optional] A `dict` with string key and string value.
- `RS256` algorithm will be used.


## Development

To install the package itself along with its dependencies, run `poetry install`.
After that you can `import py_jwt_cpp` in the virtual environment you're in.

## Tests

```
python -m pytest tests/
```

## Local Build

```
poetry install
poetry build
```

## CI Build

1. tag the ref with a name staring with `cibuildwheel`
2. Push the tag onto Github. It will trigger `cibuildwheel` workflow building wheels for:

- OS
    - `latest-ubuntu`
    - `macos-13`
    - `macos-latest`
- Python:
    - `ubuntu`: `>= 3.8`
    - `macos`: `>= 3.9`

## Release

1. Name your branch with a name staring with `build`.
2. Push it onto Github to trigger the wheel build.
3. Build `macos, python =3.8` by `poetry build`.
4. Download the wheels from Github and put them into the `dist` folder.
5. Upload it onto Pypi.

## LICENSE

MIT
