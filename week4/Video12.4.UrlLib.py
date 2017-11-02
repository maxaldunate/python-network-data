import urllib.request, urllib.parse, urllib.error

def main():
    ReadTxtFileFromWeb()
    CountTxtFileFromWeb()
    ReadHtmlFileFromWeb()
    return

def ReadHtmlFileFromWeb():
    fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
    for line in fhand:
        print(line.decode().strip())
    print()

def ReadTxtFileFromWeb():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())
    print()

def CountTxtFileFromWeb():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    counts = dict()

    for line in fhand:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        print(counts)
    print()

if __name__ == '__main__':
    main()
