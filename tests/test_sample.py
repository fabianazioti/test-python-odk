import subprocess
import sys

def test_module():
    res = subprocess.call(f'{sys.executable} -m teste', shell=True)

    assert res == 0

if __name__ == '__main__':
    import pytest

    pytest.main()
