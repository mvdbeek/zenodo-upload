import logging
import os
from urllib.parse import (
    urljoin,
    urlencode,
)
from typing import Optional

import requests

from models.depositions import Deposition
from models.files import FilesResponse

log = logging.getLogger(__name__)

# Requires PAT from zenodo: https://zenodo.org/account/settings/applications/tokens/new/

ZENODO_URL = "https://zenodo.org/"
DEPOSITIONS = "api/deposit/depositions"


def get_session(access_token: str) -> requests.Session:
    session = requests.Session()
    session.headers["access_token"] = access_token()
    return session


def check_response(response: requests.Response):
    try:
        response.raise_for_status()
    except requests.HTTPError:
        log.error("Request to %s failed: %s", response.url, response.text)
        raise


def create_upload(
    session: requests.Session, zenodo_url: str = ZENODO_URL
) -> Deposition:
    response = session.post(urljoin(zenodo_url, DEPOSITIONS))
    check_response(response)
    return Deposition.from_json(response.text)


def upload_file(
    session: requests.Session, path: str, bucket_url: str, rel_path: Optional[str]
) -> FilesResponse:
    with open(path, "rb") as fh:
        # TODO: make sure file doesn't exist
        response = session.put(
            urljoin(bucket_url, urlencode(rel_path or os.path.basename(path))), data=fh
        )
    check_response(response)
    return FilesResponse(response.json())
