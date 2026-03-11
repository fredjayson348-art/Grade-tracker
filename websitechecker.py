
import urllib.request
from datetime import datetime

websites = [
    "http://google.com",
    "http://youtube.com",
    "http://facebook.com",
    "http://wikipedia.org",
    "http://github.com"
]

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("=== Check at", now, "===")

for site in websites:
    try:
        urllib.request.urlopen(site, timeout=5)
        print("ONLINE ->", site)
    except:
        print("OFFLINE ->", site)

print()
