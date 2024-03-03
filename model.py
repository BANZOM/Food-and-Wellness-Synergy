import google.generativeai as genai
import os
from dotenv import load_dotenv
import io
import base64
from PIL import Image
from pyzbar.pyzbar import decode

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))

# for model in genai.list_models():
#     print(model)

def get_model(type='text'):
    if type == 'text':
        return genai.GenerativeModel('models/gemini-1.0-pro-latest')
    else:
        return genai.GenerativeModel('models/gemini-1.0-pro-vision-latest')

def custom_prompt(item):
    prompt = '''You are a Top Known Chef who knows variety of special dishes in India.
                When user give items as input. You tell user What is the best meal recipe made for {item}? 
                Include atleast one other extra ingredient. So to increase sale of that extra ingredient.

                Provided with the following ingredient(s): {item},

                Output Format in HTML tags only including the following details starts with h2 tag:
                    Name of Meal: [Enter Name of the Dish]
                    Preparation Time: [Enter Preparation Time]
                    Cooking Time: [Enter Cooking Time]
                    Ingredients:
                    [Main Ingredient]
                    [Extra Ingredient for Sales Boost]
                    [Additional Ingredients]
                    Directions: [Provide Step-by-Step Directions for Cooking]
                    Nutrition: [Include Nutritional Information per Serving]
                    Servings: [Specify Number of Servings]
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
    model = get_model(type='text')
    response = model.generate_content(prompt, generation_config=get_generation_config())
    print(response.text)
    return response.text

def get_recipe_from_image(image):
    print("function triggered")
    model = get_model(type='image')
    image = Image.open(image)
    bytearray = io.BytesIO()
    image.save(bytearray, format=image.format)
    bytearray = bytearray.getvalue()
    encoded_image = base64.b64encode(bytearray)

    image_blob = {
        'mime_type': 'image/jpeg', # or 'image/png'
        'data': encoded_image.decode('utf-8')
    }
    prompt = custom_prompt('the given items in the image')
    response = model.generate_content([prompt, {'inline_data': image_blob}], generation_config=get_generation_config())
    return response.text

def read_qr_code(file_path):
    try:
        with open(file_path, 'rb') as image_file:
            image = Image.open(image_file)
            decoded_objects = decode(image)

            if decoded_objects:
                # for obj in decoded_objects:
                #     print(f"Detected QR code containing: {obj.data.decode('utf-8')}")
                return decoded_objects[0].data.decode('utf-8')  # Return the decoded data
            else:
                print("No QR code found in the image.")
                return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def get_recipe_by_qr_scan(qr_code):
    print("function triggered")
    item = read_qr_code(qr_code)
    if item:
        return get_recipe(item)
    else:
        return "No QR code found in the image."
    
if __name__ == '__main__':
    item = 'milk,apple'
    # print(get_recipe(item))
    # print(get_recipe_from_image('templates/dump/images/kurkure&biscuit.png'))
    # print(get_recipe_by_qr_scan('templates/dump/images/eggsQR.png'))
    pass
