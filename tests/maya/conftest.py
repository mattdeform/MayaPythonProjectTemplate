import pytest

@pytest.fixture(autouse=True)
def run_in_maya():
    from maya import (
        standalone,
        cmds
    )
    standalone.initialize()
    cmds.scriptEditorInfo(e=True, sw=True, se=True, si=True)
