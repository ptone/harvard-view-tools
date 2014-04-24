from __future__ import print_function
import datetime
from pyquery import PyQuery as pq
import urllib2


def is_lecture(item):
    for l in item.find('ul').findall('li'):
        if 'list-type' in l.attrib['class']:
            l_id = l.attrib['id']
            if 'L' in l_id:
                return l_id
    return False


def get_date(item):
    month = item.find('div').text.strip()
    day = item.find('div').find('span').text
    dateobj = datetime.datetime.strptime("%s-%s-2013" % (month, day), "%b-%d-%Y")
    return dateobj.strftime('%Y%m%d')


def main():
    d = pq('http://cm.dce.harvard.edu/2014/01/14328/publicationListing.shtml')
    items = d('.list-asset').find('li')
    lectures = [x for x in items if (x.find('div') and 'list-date' in x.find('div').attrib['class'])]
    lecture_data_format = 'http://cm.dce.harvard.edu/2014/01/14328/{lect_num}/14328-{lect_date}-{lect_num}-H264MultipleHighLTH-16x9.xml'

    for l in lectures:
        # gets the lecture label in the form "L03"
        l_id = is_lecture(l)
        if l_id:
            print("getting: ", l_id)
            datestr = get_date(l)
            data_url = lecture_data_format.format(lect_num=l_id, lect_date=datestr)
            with open('%s.xml' % l_id, 'w') as f:
                f.write(
                    urllib2.urlopen(data_url ).read()
                )


if __name__ == "__main__":
    main()
