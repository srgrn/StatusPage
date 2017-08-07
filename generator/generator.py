from checks.http_check import *
import json


def main():
    results = {'services': []}
    check_arr = [
        BasicHttpCheck(servicename='Public Website', path='www.cnn.com', method='get'),
        BasicHttpCheck(servicename='Public with keyword', path='getbootstrap.com/', protocol='http', method='get').set_search_keyword('fails'),
    ]
    for c in check_arr:
        results['services'].append(c.run_check())

    print json.dumps(results)


if __name__ == '__main__':
    main()
