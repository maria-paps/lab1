import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

#url = 'http://python.org/'  # προσδιορισμός του url
url = input("Input URL:")

if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)
    
    print("Website headers are", url, "\n", response.headers, "\n\n")
    
    server = response.headers.get('Server')
    
    if server:
        print("The server is", server)
    else:
        print("No server found")
        
    cookies = response.headers.get('Set-Cookie')
    
    if cookies:
        print("The cookies are", cookies)
    else:
        print("No cookies found")