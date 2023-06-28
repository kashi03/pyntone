import os.path
from os import environ as env
from uuid import uuid4

import dotenv
import pytest
from pyntone import KintoneRestAPIClient, ApiTokenAuth
from pyntone.types.record import RecordForParameter


@pytest.fixture(autouse=True, scope='session')
def load_env():
    if os.path.exists('.env'):
        dotenv.load_dotenv()


@pytest.fixture(autouse=True)
def client():
    auth = ApiTokenAuth(api_token=env['API_TOKEN'])
    client = KintoneRestAPIClient(base_url=env['BASE_URL'], auth=auth)
    return client


def test_get_form_fields(client):
    result = client.app.get_form_fields(env['APP_ID'])
    assert result.get('revision') is not None
    assert result.get('properties') is not None


def test_add_form_fields(client):
    pass


def test_update_form_fields(client):
    pass


def test_delete_form_fields(client):
    result = client.app.delete_form_fields(env['APP_ID'], ['column1', 'column2'])
    assert result.get('revision') is not None


def test_get_form_layout(client):
    result = client.app.get_form_layout(env['APP_ID'])
    assert result.get('revision') is not None
    assert result.get('layout') is not None


def test_update_form_layout(client):
    pass


def test_get_views(client):
    result = client.app.get_views(env['APP_ID'])
    assert result.get('revision') is not None
    assert result.get('views') is not None


def test_update_views(client):
    pass


def test_get_app(client):
    result = client.app.get_app(env['APP_ID'])
    assert result.get('appId') is not None
