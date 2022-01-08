import json
import typing
from io import StringIO

def write_json(data : typing.Dict, buffer : typing.BinaryIO) -> None:
    
    stream = StringIO()
    json.dump(data, stream)
    stream.seek(0)
    buffer.write(stream.read().encode("UTF-8"))
