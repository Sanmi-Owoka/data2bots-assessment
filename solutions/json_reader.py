import json
from .helper_functions import checkType


def read_JSON_file(read_json_file, write_json_file):
    """read_json_file is the file that the data is read from e.g data/data_1.json"""
    """write_json_file is the file the schema response is dump into"""

    schema = {
        "type": "",
        "tag": "",
        "description": "",
        "required": False
    }

    globalObj = {}

    with open(read_json_file, "r") as f:
        content = f.read()
        # load json content
        text = json.loads(content)

        messageObj = text['message']
        attributes = messageObj.keys()

        for key in attributes:
            msg = checkType(messageObj[key])

            if msg == "INTEGER":
                integer = schema.copy()
                integer['type'] = msg.lower()
                globalObj[key] = integer

            if msg == "STRING":
                string = schema.copy()
                string['type'] = msg.lower()
                globalObj[key] = string

            if msg == "ENUM":
                enum = schema.copy()
                enum['type'] = msg.lower()
                globalObj[key] = enum

            if msg == "ARRAY":
                array = schema.copy()
                array['type'] = msg.lower()
                globalObj[key] = array

    with open(write_json_file, "w") as f:
        # dumps json response
        f.write(json.dumps(globalObj, indent=4))
