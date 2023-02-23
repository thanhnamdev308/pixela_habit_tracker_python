"""
Define handler functions to communicate with Pixela
API how to use document: https://docs.pixe.la/
"""

import requests
import json
from requests import Response

API_PREFIX = "https://pixe.la"
pixela_token = ""  # set by user, at least 8 characters
pixela_username = ""


def set_token(token: str) -> None:
    global pixela_token
    pixela_token = token


def set_username(username: str) -> None:
    global pixela_username
    pixela_username = username


def get_token() -> str:
    global pixela_token
    return pixela_token


def get_username() -> str:
    global pixela_username
    return pixela_username


# __________USER__________

def create_user() -> Response:
    """
    This function call the API endpoint
    to create a new user

    Request type:   POST
    End point:      /v1/users

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + "/v1/users"

    params = {
        "token": pixela_token,
        "username": pixela_username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    print("POST...")
    print(json.dumps(params, indent=2, default=str))

    response = requests.post(url=api_endpoint, json=params)

    return response


def update_token(new_token: str) -> Response:
    """
    This function call the API endpoint
    to update username

    Request type:   PUT
    End point:      /v1/users/<username>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}"

    params = {
        "newToken": new_token,
    }

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("PUT...")
    print(json.dumps(params, indent=2, default=str))

    response = requests.put(url=api_endpoint, json=params, headers=headers)

    return response


def delete_user() -> Response:
    """
    This function call the API endpoint
    to delete a new user

    Request type:   DELETE
    End point:      /v1/users/<username>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("DELETE...")

    response = requests.delete(url=api_endpoint, headers=headers)

    return response


# __________USER PROFILE__________

def view_user_profile(username: str) -> Response:
    """
    This function call the API endpoint
    to view a user profile

    Request type:   GET
    End point:      /@<username>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/@{username}"

    print("GET...")

    response = requests.get(url=api_endpoint)

    return response


def update_user_profile(mode: str, new_value: str) -> Response:
    """
    This function call the API endpoint
    to update a user profile

    Request type:   PUT
    End point:      /@<username>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/@{pixela_username}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    params: dict = {}

    match mode:
        case "displayName":
            params = {"displayName": new_value}
        case "gravatarIconEmail":
            params = {"gravatarIconEmail": new_value}
        case "title":
            params = {"title": new_value}
        case "timezone":
            params = {"timezone": new_value}
        case "aboutURL":
            params = {"aboutURL": new_value}
        case "pinnedGraphID":
            params = {"pinnedGraphID": new_value}

    print("PUT...")
    print(json.dumps(params, indent=2, default=str))

    response = requests.put(url=api_endpoint, headers=headers, json=params)

    return response


# __________GRAPH__________

def create_graph(graph_id: str, name: str, unit: str, data_type: str, color: str) -> Response:
    """
    This function call the API endpoint
    to create a graph

    Request type:   POST
    End point:      /v1/users/<username>/graphs

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    params = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": data_type,
        "color": color
    }

    print("POST...")
    print(json.dumps(params, indent=2, default=str))

    response = requests.post(url=api_endpoint, headers=headers, json=params)

    return response


def get_all_graph() -> Response:
    """
    This function call the API endpoint
    to get all graph definitions (information)

    Request type:   GET
    End point:      /v1/users/<username>/graphs

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("GET...")

    response = requests.get(url=api_endpoint, headers=headers)

    return response


def get_graph_def(graph_id: str) -> Response:
    """
    This function call the API endpoint
    to get a graph definitions (information)

    Request type:   GET
    End point:      /v1/users/<username>/graphs/<graphID>/graph-def

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}/graph-def"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("GET...")

    response = requests.get(url=api_endpoint, headers=headers)

    return response


def delete_graph(graph_id: str) -> Response:
    """
    This function call the API endpoint
    to delete a graph

    Request type:   DELETE
    End point:      /v1/users/<username>/graphs/<graphID>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("DELETE...")

    response = requests.delete(url=api_endpoint, headers=headers)

    return response


def display_graph(graph_id: str) -> Response:
    """
    This function call the API endpoint
    to display a graph in html format

    Request type:   GET
    End point:      /v1/users/<username>/graphs/<graphID>.html

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}.html"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("GET...")

    response = requests.get(url=api_endpoint, headers=headers)

    return response


def get_graph_pixels(graph_id: str) -> Response:
    """
    This function call the API endpoint
    to get graph's pixels list

    Request type:   GET
    End point:      /v1/users/<username>/graphs/<graphID>/pixels

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}/pixels"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("GET...")

    response = requests.get(url=api_endpoint, headers=headers)

    return response


def get_graph_stats(graph_id: str) -> Response:
    """
    This function call the API endpoint
    to get graph's statistics

    Request type:   GET
    End point:      /v1/users/<username>/graphs/<graphID>/stats

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}/stats"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("GET...")

    response = requests.get(url=api_endpoint, headers=headers)

    return response


# __________PIXEL__________

def post_pixel(graph_id: str, date: str, quantity: str) -> Response:
    """
    This function call the API endpoint
    to post a pixel to a graph

    Request type:   POST
    End point:      /v1/users/<username>/graphs/<graphID>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    params = {
        "date": date,
        "quantity": quantity
    }

    print("POST...")
    print(json.dumps(params, indent=2, default=str))

    response = requests.post(url=api_endpoint, headers=headers, json=params)

    return response


def get_pixel(graph_id: str, date: str) -> Response:
    """
    This function call the API endpoint
    to get a pixel of a graph

    Request type:   GET
    End point:      /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}/{date}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("GET...")

    response = requests.get(url=api_endpoint, headers=headers)

    return response


def update_pixel(graph_id: str, date: str, quantity: str) -> Response:
    """
    This function call the API endpoint
    to update a pixel of a graph

    Request type:   PUT
    End point:      /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}/{date}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    params = {
        "quantity": quantity
    }

    print("PUT...")
    print(json.dumps(params, indent=2, default=str))

    response = requests.get(url=api_endpoint, headers=headers, json=params)

    return response


def delete_pixel(graph_id: str, date: str) -> Response:
    """
    This function call the API endpoint
    to delete a pixel of a graph

    Request type:   DELETE
    End point:      /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

    :return: status code of the request
    """

    api_endpoint = API_PREFIX + f"/v1/users/{pixela_username}/graphs/{graph_id}/{date}"

    headers = {
        "X-USER-TOKEN": pixela_token
    }

    print("DELETE...")

    response = requests.delete(url=api_endpoint, headers=headers)

    return response
