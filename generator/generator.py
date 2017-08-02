from checks.http_check import *

def main():
    check_arr = [
        BasicHttpCheck(servicename='Public Website', path='www.cnn.com',method='get')
    ]
    for c in check_arr:
        print c.run_check()

if __name__ == '__main__':
    main()