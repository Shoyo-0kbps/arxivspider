import os
from pathlib import Path
import typing

LOCAL_PATH = str(Path(__file__).parent.parent.parent)

DS_ENV : typing.Dict[str, str] = {
    "Tests" : os.path.join(LOCAL_PATH,"tests"),
    "Datas" : os.path.join(LOCAL_PATH,"datas"),
    }

DT_EXT = ["pdf", "tar.gz", "zip"]
