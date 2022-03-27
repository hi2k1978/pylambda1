import pytest
from importlib import import_module
import sys

@pytest.fixture(scope="function", autouse=True)
def __yield():
    path = "../src/func2"
    sys.path.append(path)
    origkeys = [kk for kk in sys.modules.keys()]

    func_module = import_module(".index", "src.func2")
    yield {"module": func_module }

    delkeys = [kk for kk in sys.modules.keys() if kk not in origkeys]
    for key in delkeys: del sys.modules[key]
    sys.path.remove(path)
    
def test_func2_index(__yield):
    target = __yield["module"]
    res = target.handler({"event": "event2"}, "context2")
    print(f"{res=}")
    assert True
