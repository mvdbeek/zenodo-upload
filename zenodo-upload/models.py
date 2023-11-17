from typing import List
from typing import Any
from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass
class Links:
    bucket: str
    discard: str
    edit: str
    files: str
    html: str
    latest_draft: str
    latest_draft_html: str
    publish: str
    self: str


@dataclass
class DepositionFile:
    id: str
    filename: str
    filesize: int
    checksum: str


@dataclass
class PrereserveDoi:
    doi: str
    recid: int


@dataclass
class Metadata:
    prereserve_doi: PrereserveDoi

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        _prereserve_doi = PrereserveDoi.from_dict(obj.get("prereserve_doi"))
        return Metadata(_prereserve_doi)


@dataclass_json
@dataclass
class Deposition:
    conceptrecid: str
    created: str
    files: List[DepositionFile]
    id: int
    links: Links
    metadata: Metadata
    modified: str
    owner: int
    record_id: int
    state: str
    submitted: bool
    title: str