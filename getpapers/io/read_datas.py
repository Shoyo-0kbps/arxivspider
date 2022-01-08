import json
import typing

def load_json(buffer : typing.BinaryIO) -> typing.Dict:
    
    data = json.load(buffer)
    buffer.close()
    return data
