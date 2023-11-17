from dataclasses import dataclass


@dataclass
class Links:
    self: str
    version: str
    uploads: str


@dataclass
class FilesResponse:
    key: str
    mimetype: str
    checksum: str
    version_id: str
    size: int
    created: str
    updated: str
    links: Links
    is_head: bool
    delete_marker: bool
