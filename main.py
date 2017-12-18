from pprint import pprint

import server

def main():
    serv = server.Server(quarter='FALL', year=2017, department='ECON')

    html = serv.getRawHTML()

    pprint(html)

if __name__ == "__main__":
    main()