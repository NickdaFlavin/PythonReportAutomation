import json

def ParseAppfolioV1JSON(jsonstring: str):
    jsonstring.replace("'", '"')
    jsonstring.replace("None", '"NULL"')
    parsed_data = json.loads(jsonstring)
    return parsed_data
    


