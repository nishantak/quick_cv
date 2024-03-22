import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = "AIzaSyDbcHMuxG7If4izSr6vgAQ3gYEhEyGbTHY"

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

prompt = "The description is as follows:\n"

def modify_des(description):
    global prompt
    prompt = prompt + description
    return model.generate_content(prompt).text

if __name__ == '__main__':
    print(modify_des("say hi"))
    print(prompt)
 
