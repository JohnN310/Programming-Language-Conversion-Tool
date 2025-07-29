import google.generativeai as genai
from dotenv import load_dotenv
import os 
class CustomLLM:
    def __init__(self):
        pass

    def generate_response(self, prompt):
        load_dotenv()
        api_key = os.getenv("api_key")
        model = os.getenv("model")        
        genai.configure(api_key= api_key)
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt)
        return response.text

# class CustomLLM: 
#     def __init__(self):
#         pass

#     def generate_response(self, agent_prompt, user_prompt):
#         load_dotenv()
#         api_key = OpenAI(api_key= os.getenv("gpt_api_key"))
#         model = os.getenv("gpt_model")        
#         response = api_key.chat.completions.create(
#             model=model,
#             messages=[
#                 {"role": "system", "content": agent_prompt},
#                 {"role": "user", "content": user_prompt},
#             ],
#             temperature=0.2,
#         )
#         return response.choices[0].message.content
    