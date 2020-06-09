import urllib.request
import json

id = '12018' # 12018 is an example ID

print('Downloading scenario with ID: ' + id + '...')

getUrl = urllib.request.urlopen('http://s.ndemiccreations.com/plague/scenarios_download?id=' + id) # Submitting request for a new download URL to Ndemic Creations' servers
downloadUrlJSON = getUrl.read()
downloadUrlParsed = json.loads(downloadUrlJSON) # Parsing response in JSON
downloadUrl = downloadUrlParsed['downloadUrl'] # Getting one-off direct download URL of scenario in ZIP archive
urllib.request.urlretrieve(downloadUrl, id + '.zip') # Downloading scenario in ZIP

print('Scenario downloaded successfully.')