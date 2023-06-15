import json
from urllib.request import urlopen


def transform(indicator_name):
    with open(f"definition_files/{indicator_name}_definition.json") as f:
        indicator_definition = json.load(f)

    metadata_data = []
    for country_data in indicator_definition["fields"]["country-specific"]:
        dataset_id = country_data["dataset_id"]
        metadata_url = (
            f"https://data.humdata.org/dataset/{dataset_id}/"
            f"download_metadata?format=json"
        )
        metadata_data_country = json.loads(urlopen(metadata_url).read())
        metadata_keys = [
            "title",
            "name",
            "notes",
            "dataset_source",
            "organization",
            "dataset_date",
            "last_modified",
            "data_update_frequency",
        ]
        metadata_data_country = {
            key: metadata_data_country[key] for key in metadata_keys
        }
        metadata_data_country["hdx_id"] = dataset_id
        metadata_data_country[
            "dataset_date_range"
        ] = metadata_data_country.pop("dataset_date")
        metadata_data.append(metadata_data_country)
    return metadata_data
