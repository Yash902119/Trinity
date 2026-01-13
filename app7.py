import google.generativeai as genai
genai.configure(api_key="AIzaSyCGEoHRopKXpHtegvY7GmAhk4eYxBMVZP8")
for m in genai.list_models():
    print(m.name)