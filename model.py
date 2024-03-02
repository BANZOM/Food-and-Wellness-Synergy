from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

# for model in genai.list_models():
#     print(model)

model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

def custom_prompt(item):
    prompt = '''You are a Top Known Chef who knows variety of special dishes in India.
                When user give items as input. You tell user What is the best top 3 meal recipe made from {item}? 
                Include atleast one other extra ingredient. So to increase sale of that extra ingredient.
                Output should be html formatted. only show the body of the html. without printing body tag.
                Output Format: 
                Give Name of Meal (in heading tags)
                Preparation Time (in italic)
                Cooking Time (in italic)
                Ingredients (in bullet points)
                Directions (in numbered list)
                Nutrition   (in table)
                Servings    (in bold)
            '''.format(item=item)
    return prompt

def get_recipe(item,):
    prompt = custom_prompt(item)
    return model.generate_content(prompt).text

if __name__ == '__main__':
    item = 'milk'
    print(get_recipe(item))
    pass
