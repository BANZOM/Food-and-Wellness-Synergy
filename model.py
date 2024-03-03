from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

import io
import base64
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

for model in genai.list_models():
    print(model)

model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

def get_model(type='text'):
    if type == 'text':
        return genai.GenerativeModel('models/gemini-1.0-pro-latest')
    else:
        return genai.GenerativeModel('models/gemini-1.0-pro-vision-latest')

def custom_prompt(item):
    prompt = '''You are a Top Known Chef who knows variety of special dishes in India.
                When user give items as input. You tell user What is the best meal recipe made for {item}? 
                Include atleast one other extra ingredient. So to increase sale of that extra ingredient.
                Output should be in body format. 
                Output Format: 
                Give Name of Meal
                Preparation Time
                Cooking Time
                Ingredients
                Directions
                Nutrition
                Servings
            '''.format(item=item)
    return prompt

def get_generation_config():
    return genai.GenerationConfig(
        temperature=0.3,
        top_p=1.0,
    )

def get_recipe(item):
    print("function triggered")
    prompt = custom_prompt(item)
    response = model.generate_content(prompt, generation_config=get_generation_config())
    print(response.text)
    return response.text

def get_recipe_from_image(image):
    print("function triggered")
    model = get_model(type='image')
    image = Image.open(image)
    bytearray = io.BytesIO()
    image.save(bytearray, format=image.format)
    response = model.generate_content(image, generation_config=get_generation_config())
    return response.text

if __name__ == '__main__':
    item = 'milk,apple'
    # print(get_recipe(item))
    pass
