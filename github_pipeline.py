"""A template that is a good start for vibe coding REST API Source. Works best with `dlt ai` command cursor rules"""

import dlt
from dlt.sources.rest_api import (
    RESTAPIConfig,
    rest_api_resources,
)

# GitHub REST API Source for 'repositories' endpoint
@dlt.source
def github_source(owner: str = dlt.secrets.value, access_token: str = dlt.secrets.value):
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.github.com/",
            "auth": {
                "type": "bearer",
                "token": access_token,
            },
        },
        "resources": [
            {
                "name": "repositories",
                "endpoint": {
                    "path": f"users/{owner}/repos",
                    "method": "GET"
                }
            }
        ],
    }
    yield from rest_api_resources(config)



def get_data() -> None:
    pipeline = dlt.pipeline(
        pipeline_name='github_pipeline',
        destination='duckdb',
        dataset_name='github_data',
        progress="log"
    )
    # Load values from secrets.toml
    owner = dlt.secrets["owner"]
    access_token = dlt.secrets["access_token"]
    load_info = pipeline.run(github_source(owner, access_token))
    print(load_info)


if __name__ == "__main__":
    get_data()
