import subprocess
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    subprocess.run(["poetry", "install"], check=True)
