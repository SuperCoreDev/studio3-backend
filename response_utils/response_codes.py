from enum import Enum


class ResponseCodes(Enum):
    NEW_REGISTRATION = "NEW_REGISTRATION"
    LOGIN_SUCCESS = "LOGIN_SUCCESS"
    NOT_LOGGED_IN = "NOT_LOGGED_IN"
    USER_PROFILE_UPDATE_SUCCESS = "USER_PROFILE_UPDATE_SUCCESS"
    UPLOAD_SUCCESS = "UPLOAD_SUCCESS"
