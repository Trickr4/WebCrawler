import pickle

class Response(object):
    def __init__(self, resp_dict):
        print("res")

        self.url = resp_dict["url"]
        self.status_code = resp_dict["status"]
        self.error = resp_dict["error"] if "error" in resp_dict else None
        try:
            self.raw_response = (
                pickle.loads(resp_dict["response"])
                if "response" in resp_dict else
                None)
        except TypeError:
            self.raw_response = None
