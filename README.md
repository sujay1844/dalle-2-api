# DALL-E 2

DALL-E is an image generator AI developed by OpenAI. It takes in a natural language input to generate or manipulate images.

This script is a client to the new API launched in public beta.

You need an API key to use it.
The  API key requires email and phone number. So I won't be sharing it.
For free you get 15 image generations every month.
The good thing is that if the image you requested already exists, it won't be charged in those 15 credits.

# Installation
- Install `openai`,
```bash
pip install openai
```

# Usage
- Provide API key. Store the API key in `.api_key.txt`
- Run the script,
```bash
python dalle-2-api.py
```
- The script will launch a browser automatically.
- It will also save the results in `dalle2.log.json`
