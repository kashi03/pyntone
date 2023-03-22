from typing import TypedDict, Union, Optional
from pyntone.types import RecordID, Revision

class RecordItem(TypedDict):
    value: Union[int, str]

RecordForParameter = dict[str, RecordItem]

class UpdateKey(TypedDict):
    field: str
    value: str

class UpdateRecordForParameter(TypedDict):
    id: RecordID
    record: Optional[RecordForParameter]
    revision: Optional[Revision]

class UpdateKeyRecordForParameter(TypedDict):
    updateKey: UpdateKey
    record: Optional[RecordForParameter]
    revision: Optional[Revision]