import openai
import webbrowser
import datetime
import json

openai.api_key_path = ".api_key.txt"

term = input("Enter some text: ")

# Get a URL of the generated image from DALL-E 2
response = openai.Image.create(
    prompt = term,
    n = 1,
    size = "1024x1024"
)
image_url = response['data'][0]['url']

# Open image in web browser and print it out as well
webbrowser.open_new(image_url)
print(image_url)

# Save results to dalle2.log.json
with open("dalle2.log.json", "r+") as logfile:
    file_data = json.load(logfile)
    logtext = {
        "timestamp": str(datetime.datetime.now()),
        "term": term,
        "image_url": image_url,
    }
    file_data['data'].append(logtext)
    logfile.seek(0)
    json.dump(file_data, logfile, indent=4)
