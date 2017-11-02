import urllib.request, urllib.parse, urllib.error

def main():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())

if __name__ == '__main__':
    main()
