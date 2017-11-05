#Unicode chasrs & strings

def Python27():
    byte = b'/&%(/&%'
    print(type(byte)) # <class 'str'>
    string = '/&%(/&%'
    print(type(string)) # <class 'str'>
    unicode = u'/&%(/&%'
    print(type(unicode))  #<type 'unicode'>

def Python35():
    byte = b'/&%(/&%'
    print(type(byte)) # <class 'bytes'>
    string = '/&%(/&%'
    print(type(string)) # <class 'str'>
    unicode = u'/&%(/&%'
    print(type(unicode))  #<type 'str'>

if __name__ == '__main__':
    #Python35()
    Python27()
