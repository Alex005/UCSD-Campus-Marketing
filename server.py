import pprint

from tinydb.database import TinyDB

from datetime import date
import re

import grequests
import requests
from bs4 import BeautifulSoup

class Server:

    _post_data = {
        'selectedTerm': '',
        'loggedIn': 'false',
        'selectedSubjects': '',
        '_selectedSubjects': '1',
        'schedOption1': 'true',
        '_schedOption1': 'on',
        '_schedOption11': 'on',
        '_schedOption12': 'on',
        'schedOption2': 'true',
        '_schedOption2': 'on',
        '_schedOption4': 'on',
        '_schedOption5': 'on',
        '_schedOption3': 'on',
        '_schedOption7': 'on',
        '_schedOption8': 'on',
        '_schedOption13': 'on',
        '_schedOption10': 'on',
        '_schedOption9': 'on',
        '_selectedDepartments': '1',
        'schedOption1Dept': 'true',
        '_schedOption1Dept': 'on',
        '_schedOption11Dept': 'on',
        '_schedOption12Dept': 'on',
        'schedOption2Dept': 'true',
        '_schedOption2Dept': 'on',
        '_schedOption4Dept': 'on',
        '_schedOption5Dept': 'on',
        '_schedOption3Dept': 'on',
        '_schedOption7Dept': 'on',
        '_schedOption8Dept': 'on',
        '_schedOption13Dept': 'on',
        '_schedOption10Dept': 'on',
        '_schedOption9Dept': 'on',
        'schDayDept': 'M',
        '_schDayDept': 'on',
        'schDayDept': 'T',
        '_schDayDept': 'on',
        'schDayDept': 'W',
        '_schDayDept': 'on',
        'schDayDept': 'R',
        '_schDayDept': 'on',
        'schDayDept': 'F',
        '_schDayDept': 'on',
        'schDayDept': 'S',
        '_schDayDept': 'on',
        'schStartTimeDept': '12:00',
        'schStartAmPmDept': '0',
        'schEndTimeDept': '12:00',
        'schEndAmPmDept': '0'
    }

    _base_url = 'https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm'

    _term, _quarter, _year, _department = '', '', 0, ''

    _html = ''

    def __init__(self, quarter, year, department):
        if str(quarter).upper() in ('FALL', 'WINTER', 'SPRING'):
            self._quarter = str(quarter).upper()[:2]
        else:
            raise ValueError
        current_year = date.today().year
        if year in (current_year - 1, current_year, current_year + 1):
            self._year = str(year)[2:]
        else:
            raise ValueError
        self._term = self._quarter + self._year
        self._department = str(department).upper()

    def getRawHTML(self):
        self._post_data['selectedTerm'] = self._term
        self._post_data['selectedSubjects'] = self._department

        req = requests.post(self._base_url, self._post_data)

        total_pages = self._getNumPages(BeautifulSoup(req.content, 'lxml'))

        urls = [self._base_url + '?page=' + str(1 + currentPage) for currentPage in range(total_pages)]

        _html_list = (grequests.post(u, data=self._post_data) for u in urls)

        _raw_html = ''

        for elm in grequests.map(_html_list):
            _raw_html += elm.text + '\n'

        return _raw_html

    def _getNumPages(self, html):
        table = html.find_all('table')[-1].find_all('td')[2]
        s = re.search('of\s+(\d+)', table.get_text())
        return int(s.group(1))

    def getNextLecture(self):
        pass
    def getNextSection(self):
        pass

course_data = {}

data = {
    'selectedTerm': '',
    'loggedIn': 'false',
    'selectedSubjects': '',
    '_selectedSubjects': '1',
    'schedOption1': 'true',
    '_schedOption1': 'on',
    '_schedOption11': 'on',
    '_schedOption12': 'on',
    'schedOption2': 'true',
    '_schedOption2': 'on',
    '_schedOption4': 'on',
    '_schedOption5': 'on',
    '_schedOption3': 'on',
    '_schedOption7': 'on',
    '_schedOption8': 'on',
    '_schedOption13': 'on',
    '_schedOption10': 'on',
    '_schedOption9': 'on',
    '_selectedDepartments': '1',
    'schedOption1Dept': 'true',
    '_schedOption1Dept': 'on',
    '_schedOption11Dept': 'on',
    '_schedOption12Dept': 'on',
    'schedOption2Dept': 'true',
    '_schedOption2Dept': 'on',
    '_schedOption4Dept': 'on',
    '_schedOption5Dept': 'on',
    '_schedOption3Dept': 'on',
    '_schedOption7Dept': 'on',
    '_schedOption8Dept': 'on',
    '_schedOption13Dept': 'on',
    '_schedOption10Dept': 'on',
    '_schedOption9Dept': 'on',
    'schDayDept': 'M',
    '_schDayDept': 'on',
    'schDayDept': 'T',
    '_schDayDept': 'on',
    'schDayDept': 'W',
    '_schDayDept': 'on',
    'schDayDept': 'R',
    '_schDayDept': 'on',
    'schDayDept': 'F',
    '_schDayDept': 'on',
    'schDayDept': 'S',
    '_schDayDept': 'on',
    'schStartTimeDept': '12:00',
    'schStartAmPmDept': '0',
    'schEndTimeDept': '12:00',
    'schEndAmPmDept': '0'
}


def getData(term, department):
    '''
    Request department course data
    :param term:
    Specific term to research (FA, WI, SP followed by YY year)
    :param department:
    Department code, find on UCSD website
    :return:
    tuple of course codes and raw course data with minimal formatting
    '''
    data['selectedTerm'] = term
    data['selectedSubjects'] = department

    url = 'https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudentResult.htm'
    r = requests.post(url, data)

    numPages = isMultiPage(BeautifulSoup(r.content, 'lxml'))

    urls = [url + '?page=' + str(1 + currentPage) for currentPage in range(numPages)]

    rs = (grequests.post(u, data=data) for u in urls)

    courseCodes = []
    courses = None
    for elm in grequests.map(rs):
        page = parsePage(BeautifulSoup(elm.text, 'lxml'))
        if courses is None:
            courses = page[1]
        else:
            courses.update(page[1])

        courseCodes += page[0]

    return courseCodes, courses


def isMultiPage(soup):
    table = soup.find_all('table')[-1].find_all('td')[2]
    s = re.search('of\s+(\d+)', table.get_text())
    return int(s.group(1))


def parsePage(soup):
    '''
    Parse the raw HTML using BeautifulSoup4 to return only relevant information
    :param soup:
    :return:
    '''

    tds = [td for td in soup.find('table', class_='tbrdr').find_all('td')]

    headerIndex = 0
    courses = {}
    courseCodes = []
    currentCourseCode = ''
    currentCourseAppendix = 1
    currentSection = []
    prevCourseCode = 0

    for td in tds:
        if 'class' in td.attrs and td['class'][0] == 'crsheader':
            if headerIndex == 2:
                matches = re.search('^(.+)\s+',td.get_text().strip())
                courses[currentCourseCode]['title'] = matches.group(1).strip()

            elif td.get_text() and td.get_text()[0].isnumeric():
                if td.get_text() != prevCourseCode:
                    prevCourseCode = td.get_text()
                    currentCourseAppendix = 1
                else:
                    currentCourseAppendix += 1
                currentCourseCode = td.get_text() + '-' + str(currentCourseAppendix)
                courseCodes.append(currentCourseCode)
                courses[currentCourseCode] = {'sections': []}

            headerIndex += 1

        elif 'class' in td.attrs and td['class'][0] == 'brdr':
            if 'border' in td.attrs and currentSection != []:
                courses[currentCourseCode]['sections'].append(currentSection)
                currentSection = []

            content = td.get_text().strip()
            if content != '':
                currentSection.append(content)

            headerIndex = 0

    if len(currentSection) > 4:
        courses[currentCourseCode]['sections'].append(currentSection)

    return courseCodes, courses
