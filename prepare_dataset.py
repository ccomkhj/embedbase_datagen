import configparser
from pathlib import Path
from typing import Tuple

import yaml
from embedbase_client.client import EmbedbaseClient


def readConfigs(path: str, globalMode: bool = False) -> Tuple[str]:
    config = configparser.ConfigParser()
    config.read(path)

    if globalMode:
        global openai_api_key, embedbase_key, embedbase_url

    openai_api_key = config["OPENAI"]["OPENAI_API_KEY"]
    embedbase_key = config["EMBEDBASE"]["EMBEDBASE_KEY"]
    embedbase_url = config["EMBEDBASE"]["EMBEDBASE_URL"]
    return openai_api_key, embedbase_key, embedbase_url


def createDataset(yamlPath: str, configPath: str):
    _, embedbase_key, embedbase_url = readConfigs(configPath)

    client = EmbedbaseClient(embedbase_url, embedbase_key)

    # TODO: read yaml and loop over files
    with open(yamlPath, "r") as stream:
        try:
            documents = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    dataset_id = Path(yamlPath).stem  # name of file is dataset_id.
    result = client.dataset(dataset_id).clear()  # reset first.

    for doc in documents["content"]:
        result = client.dataset(dataset_id).add(doc["data"], doc["metadata"])
        print(result)


if __name__ == "__main__":
    createDataset("docs/OUIF.yaml", "secrets.ini")
