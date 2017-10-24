import requests

class AppAnnieApi:
    def __init__(self, apikey):
        self.apikey = apikey

    def accounts(self):
        result = None
        header = {"authorization": "bearer {}".format(self.apikey)}
        result =  requests.get("https://api.appannie.com/v1.2/accounts",headers=header)

        if not result.ok:
            raise ValueError(
                'Response to API call is not OK. HTTP Response received from server : {} '.format(result.status_code))



        return result.json()