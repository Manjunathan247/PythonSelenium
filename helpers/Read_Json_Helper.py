import json

configuration_file_path = "./JsonFiles/configuration.json"
testdata_file_path = "./JsonFiles/testdata.json"


def readjsonfile(filepath):
    with open(filepath) as file:
        json_file = json.load(file)
    return json_file


def data_read(attribute):
    testdata = readjsonfile(testdata_file_path)
    return testdata[attribute]


def config_read(attribute):
    configdata = readjsonfile(configuration_file_path)
    return configdata[attribute]
