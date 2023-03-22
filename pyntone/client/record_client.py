from typing import Optional, TypedDict, Union, TypeVar

from pyntone.http.http_client import HttpClent, KintoneRequestParams
from pyntone.types.record import (RecordForParameter, UpdateKey,
                                  UpdateKeyRecordForParameter, UpdateRecordForParameter)
from pyntone.types import AppID, RecordID, Revision
from pyntone.url import build_path

class RecordClient:
    def __init__(self, client: HttpClent, bulk_request_client, guest_space_id: Union[int, str, None]) -> None:
        self.client = client
        self.bulk_request_client = bulk_request_client
        self.guest_space_id = guest_space_id
        self.did_warn_maximum_offset_value = False
    
    def get_record(self, app: AppID, record_id: RecordID):
        path = self.__build_path_with_guest_space_id(endpoint_name='record')
        params = KintoneRequestParams(
            app=app,
            id=record_id
        )
        return self.client.get(path, params)

    def add_record(self, app: AppID, record: Optional[RecordForParameter] = None):
        path = self.__build_path_with_guest_space_id(endpoint_name='record')
        params = KintoneRequestParams(
            app=app,
            record=record
        )
        return self.client.post(path, params)

    def update_record(
        self,
        app: AppID,
        record_id: Optional[RecordID] = None,
        update_key: Optional[UpdateKey] = None,
        record: Optional[RecordForParameter] = None,
        revision: Optional[Revision] = None
    ):
        if record_id is None and update_key is None:
            raise ValueError()
        path = self.__build_path_with_guest_space_id(endpoint_name='record')
        params = KintoneRequestParams(
            app=app,
            id=record_id,
            update_key=update_key,
            record=record,
            revision=revision
        )
        return self.client.put(path, params)

    # TODO
    def upsert_record(
        self,
        app: AppID,
        update_key: UpdateKey,
        record: Optional[RecordForParameter] = None,
        revision: Optional[Revision] = None
    ):
        raise NotImplementedError()

    def get_records(
        self,
        app: AppID,
        fields: Optional[list[str]] = None,
        query: Optional[str] = None,
        total_count: Optional[bool] = None
    ):
        path = self.__build_path_with_guest_space_id(endpoint_name='records')
        params = KintoneRequestParams(
            app=app,
            fields=fields,
            query=query,
            total_count=total_count
        )
        return self.client.get(path, params)

    def add_records(self, app: AppID, records: list[RecordForParameter]):
        path = self.__build_path_with_guest_space_id(endpoint_name='records')
        params = KintoneRequestParams(
            app=app,
            records=records
        )
        return self.client.post(path, params)
    
    def update_records(
        self,
        app: AppID,
        records: Union[list[UpdateRecordForParameter], list[UpdateKeyRecordForParameter], list[Union[UpdateRecordForParameter, UpdateKeyRecordForParameter]]]
    ):
        path = self.__build_path_with_guest_space_id(endpoint_name='records')
        params = KintoneRequestParams(
            app=app,
            records=records
        )
        return self.client.put(path, params)
    
    def delete_records(self, app: AppID, ids: list[RecordID], revisions: Optional[list[Revision]]):
        path = self.__build_path_with_guest_space_id(endpoint_name='records')
        params = KintoneRequestParams(
            app=app,
            ids=ids,
            revisions=revisions
        )
        return self.client.delete(path, params)
    
    def create_cursor(self,
        app: AppID,
        fields: Optional[list[str]] = None,
        query: Optional[str] = None,
        size: Union[int, str, None] = None
    ):
        path = self.__build_path_with_guest_space_id(endpoint_name='records/cursor')
        params = KintoneRequestParams(
            app=app,
            fields=fields,
            query=query,
            size=size
        )
        return self.client.post(path, params)
    
    def get_records_by_cursor(self, cursor_id: str):
        path = self.__build_path_with_guest_space_id(endpoint_name='records/cursor')
        params = KintoneRequestParams(
            id=cursor_id
        )
        return self.client.get(path, params)
    
    def delete_cursor(self, cursor_id: str):
        path = self.__build_path_with_guest_space_id(endpoint_name='records/cursor')
        params = KintoneRequestParams(
            id=cursor_id
        )
        return self.client.delete(path, params)
    
    def get_all_records(self):
        raise NotImplementedError()
    
    def get_all_records_with_id(self):
        raise NotImplementedError()

    def __get_all_records_Recursive_with_id(self):
        raise NotImplementedError()
    
    def get_all_records_with_cursor(self):
        raise NotImplementedError()
    
    def add_all_records(self):
        raise NotImplementedError()
    
    def __add_all_records_recursive(self):
        raise NotImplementedError()
    
    def __add_all_records_with_cursor(self):
        raise NotImplementedError()

    def update_all_records(self):
        raise NotImplementedError()
    
    def update_all_records_recursiv(self):
        raise NotImplementedError()
    
    def __update_all_records_with_bulk_request(self):
        raise NotImplementedError()
    
    def delete_all_reocrds(self):
        raise NotImplementedError()
    
    def __delete_all_records_recursive(self):
        raise NotImplementedError()
    
    def __delete_all_records_with_cursor(self):
        raise NotImplementedError()
    
    def separate_array_recursive(self):
        raise NotImplementedError()
    
    def add_record_comment(self):
        raise NotImplementedError()
    
    def delete_record_comment(self):
        raise NotImplementedError()
    
    def get_record_comments(self):
        raise NotImplementedError()
    
    def update_record_assigness(self):
        raise NotImplementedError()
    
    def update_record_status(self):
        raise NotImplementedError()
    
    def update_records_status(self):
        raise NotImplementedError()
    
    def __build_path_with_guest_space_id(self, endpoint_name: str) -> str:
        return build_path(
            endpoint_name=endpoint_name,
            guest_space_id=self.guest_space_id
        )