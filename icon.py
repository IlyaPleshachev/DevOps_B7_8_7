import os
import requests

siteurl = os.environ.get('SITEURL')

filename = "favicon.ico"
print(f"Downloading favicon for {siteurl}")
faviconurl = siteurl + "/" + filename
print('Full url: ' + faviconurl)


icon = requests.get(faviconurl, allow_redirects=True)
open(filename, 'wb').write(icon.content)

print(f"FavIcon downloaded to {filename}")
