import base_check
import requests
import json

class BasicHttpCheck(base_check.Check):
    """simple class to test if an http is available """

    def __init__(self,servicename, path, protocol='https', method='get', headers={}, payload=None):
        super(BasicHttpCheck, self).__init__(servicename)
        self.url = '{}://{}'.format(protocol, path)
        self.headers = headers
        self.payload = payload
        self.serach_on_page = None
        self.method = method

    def set_search_keyword(self, keyword):
        self.serach_on_page = keyword

    def run_check(self):
        result = {'servicename':self.servicename,'checktype': self.__class__.__name__, 'url': self.url, 'timestamp': self.get_current_epoch_millis()}

        try:
            response = requests.request(method=self.method, url=self.url, headers=self.headers, data=self.payload)
            result['elapsed'] = response.elapsed.total_seconds()
            response.raise_for_status()
            if self.serach_on_page is not None:
                if self.serach_on_page not in response.text:
                    raise ValueError('Missing keyword in result')
            result['status'] = 'OK'
        except Exception as e:
            print e
            result['status'] = 'Failure'

        return json.dumps(result)