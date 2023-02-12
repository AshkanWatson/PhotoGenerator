import requests
import json


def generate_image(prompt):
    api_key = input('Write Your OpenAI API : ')
    api_url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"1024x1024",
        "response_format":"url"
    }
    """
    response = requests.post(api_url, headers=headers, data=data)
    if response.status_code != 200:
        raise ValueError("Failed to generate image")
    response_text = json.loads(response.text)
    return response_text['data'][0]['url']


prompt = input('The Prompt To Image : ')
image_url = generate_image(prompt)
print(image_url)



