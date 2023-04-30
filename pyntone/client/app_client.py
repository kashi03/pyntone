from typing import Literal, Optional, Union
from pyntone.http.http_client import HttpClent, KintoneRequestParams
from pyntone.url import build_path

class AppClient:
    def __init__(
        self,
        client: HttpClent,
        guest_space_id: Union[int, str, None]
    ) -> None:
        self.client = client
        self.guest_space_id = guest_space_id
    
    def get_form_fields(self):
        raise NotImplementedError()

    def add_form_fields(self):
        raise NotImplementedError()
    
    def update_form_fields(self):
        raise NotImplementedError()
    
    def delete_form_fields(self):
        raise NotImplementedError()
    
    def get_form_layout(self):
        raise NotImplementedError()
    
    def update_form_layout(self):
        raise NotImplementedError()
    
    def get_views(self):
        raise NotImplementedError()
    
    def update_views(self):
        raise NotImplementedError()
    
    def get_app(self):
        raise NotImplementedError()
    
    def get_apps(self):
        raise NotImplementedError()
    
    def add_app(self):
        raise NotImplementedError()
    
    def get_app_settings(self):
        raise NotImplementedError()
    
    def update_app_settings(self):
        raise NotImplementedError()
    
    def get_process_management(self):
        raise NotImplementedError()
    
    def update_process_management(self):
        raise NotImplementedError()
    
    def get_deploy_status(self):
        raise NotImplementedError()
    
    def deploy_app(self):
        raise NotImplementedError()
    
    def get_field_acl(self):
        raise NotImplementedError()
    
    def update_field_acl(self):
        raise NotImplementedError()
    
    def get_app_acl(self):
        raise NotImplementedError()
    
    def update_app_acl(self):
        raise NotImplementedError()

    def evaluate_records_acl(self):
        raise NotImplementedError()
    
    def get_record_acl(self):
        raise NotImplementedError()
    
    def update_record_acl(self):
        raise NotImplementedError()
    
    def get_app_customize(self):
        raise NotImplementedError()
    
    def update_app_customize(self):
        raise NotImplementedError()
    
    def get_general_notifications(self):
        raise NotImplementedError()

    def update_general_notifications(self):
        raise NotImplementedError()
    
    def get_per_record_notifications(self):
        raise NotImplementedError()
    
    def update_per_record_notifications(self):
        raise NotImplementedError()
    
    def get_reminder_notifications(self):
        raise NotImplementedError()
    
    def update_reminder_notifications(self):
        raise NotImplementedError()

    def get_reports(self):
        raise NotImplementedError()
    
    def update_reports(self):
        raise NotImplementedError()
    
    def get_app_actions(self):
        raise NotImplementedError()
    
    def update_app_actions(self):
        raise NotImplementedError()
    
    def __build_path_with_guest_space_id(
        self,
        endpoint_name: str,
        preview: bool = False
    ) -> str:
        return build_path(
            endpoint_name=endpoint_name,
            guest_space_id=self.guest_space_id,
            preview=preview
        )