from typing import Union

from pydantic import BaseModel


class ApiTokenAuth(BaseModel):
    __type = 'apiToken'
    api_token: Union[str, list[str]]

class PasswordAuth(BaseModel):
    __type = 'password'
    user_name: str
    password: str

class OAuthTokenAuth(BaseModel):
    __type = 'oAuthToken'
    oauth_token: str

DiscriminatedAuth = Union[ApiTokenAuth, PasswordAuth, OAuthTokenAuth]

class BasicAuth(BaseModel):
    user_name: str
    password: str