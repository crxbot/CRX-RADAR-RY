import urllib.request
import ssl
import certifi
import os
from datetime import datetime

BASE_URL = "https://opendata.dwd.de/weather/radar/radolan/ry"
FILENAME = "raa01-ry_10000-latest-dwd---bin.hdf5"

OUTPUT_DIR = "data/radar"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ssl_context = ssl.create_default_context(cafile=certifi.where())

url = f"{BASE_URL}/{FILENAME}"
print("Downloading:", url)

# Download
with urllib.request.urlopen(url, context=ssl_context, timeout=30) as response:
    data = response.read()

# Zeitstempel für lokale Datei (optional, aber sinnvoll)
now = datetime.utcnow()
output_path = os.path.join(
    OUTPUT_DIR,
    f"radolan-ry-latest.hdf5"
)

with open(output_path, "wb") as f:
    f.write(data)

print("Saved:", output_path)
