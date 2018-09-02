from gtts import gTTS
import json
from pprint import pprint

with open('voices.json') as f:
    data = json.load(f)
for i in range(2):
    tts = gTTS(data[i]['texto'], lang='pt-br')
    tts.save(data[i]['arquivo'])