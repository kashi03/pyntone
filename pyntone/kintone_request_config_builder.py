import base64
import json
from enum import Enum
from urllib.parse import urljoin

from pyntone.types.auth import ApiTokenAuth, DiscriminatedAuth, PasswordAuth


class HttpMethod(Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'

class KintoneRequestParams:
    def __init__(self, **kargs) -> None:
        self.params = kargs
    
    def build_url_params(self):
        url_params = {}
        for key, value in self.params.items():
            if value is None:
                continue
            value_type = type(value)
            if value_type is list:
                url_params.update(self.__list2urlquery(key, value))
            elif value_type is bool:
                url_params[key] = str(value).lower()
            elif value_type is str or value_type is int:
                url_params[key] = value
            else:
                raise ValueError(f'The parameter contains a value that cannot be used as a URL parameter.')
        return url_params
    
    def __list2urlquery(self, name: str, value: list):
        return { f'{name}[{index}]': v for index, v in enumerate(value) if v is not None }
    
    def build_payload(self):
        return { key: value for key, value in self.params.items() }

class KintoneRequestConfigBuilder():
    def __init__(self, auth: DiscriminatedAuth, base_url: str) -> None:
        self.auth = auth
        self.base_url = base_url
    
    def build(self, method: HttpMethod, path: str, params: KintoneRequestParams) -> dict:
        config = {
            'method': method.value,
            'url': urljoin(self.base_url, path),
            'headers': self.__build_headers(method, self.auth),
        }
        if method == HttpMethod.GET:
            url_params = params.build_url_params()
            config['params'] = url_params
        elif method == HttpMethod.POST:
            payload = params.build_payload()
            config['data'] = json.dumps(payload)
        elif method == HttpMethod.PUT:
            payload = params.build_payload()
            config['data'] = json.dumps(payload)
        elif method == HttpMethod.DELETE:
            payload = params.build_payload()
            config['data'] = json.dumps(payload)
        else:
            raise NotImplementedError('Unimplemented method.')
        return config
    
    def __build_headers(self, method: HttpMethod, auth: DiscriminatedAuth) -> dict[str, str]:
        if type(auth) is ApiTokenAuth:
            api_token = auth.api_token
            if type(api_token) is not str:
                api_token = ','.join(api_token)
            headers = {
                'X-Cybozu-API-Token': api_token
            }
            if method != HttpMethod.GET:
                headers['Content-Type'] = 'application/json'
            return headers
        elif type(auth) is PasswordAuth:
            password = auth.password
            user_name = auth.user_name
            b64_pass = base64.b64encode(f'{user_name}:{password}'.encode()).decode()
            headers = {
                'X-Cybozu-Authorization':b64_pass,
            }
            if method != HttpMethod.GET:
                headers['Content-Type'] = 'application/json'
            return headers
        else:
            raise NotImplementedError('Unimplemented authentication method. Please use ApiTokenAuth or PasswordAuth.')
