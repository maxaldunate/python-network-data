import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def main():
    url = input('Enter -')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        print(tag.get('href',None))

    return


if __name__ == '__main__':
    main()
