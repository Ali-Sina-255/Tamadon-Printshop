from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested profile is not exist."


class NotYourAccount(APIException):
    default_detail = "You can't edit a profile that doesn't belong to you ."
