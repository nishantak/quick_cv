from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

"""
    Our current prototype implementation employs pre-exisitng LLM, such as Gemini in this case since it is free.
    For the scope of implementation of the idea training an NLP model using thousands of accepted resume data available online is perfectly viable.
    TF-IDF can be used to extract Industry Specific Data, Job context and a mapping using regeression can be mathematically defined 
    that transforms input data into a model data.

    However, for the scope of this hackathon training such a model cannot be performed within the 36 Hours timeline, given the computaional
    capabilites of our machines. Hence, a simpler implementation using pre-exsiting models have been inlcuded as a proof-of-concept.
"""

# These keywords were the common denominator in various resumes online.
# While here this has been done manually, in the implementation we describe above it will be done using NLP making the collection much more valuable! 
keywords = "algorithms, architecture, migration, development, framework, analytical, etc."

def modify_des(context, description, type):
    """
        The prompt has beeen designed keeping in mind the working of Genertive AI models. 
        We browsed several articles on streamlining prompts for the best and most effetive response and then designed the prompt.
        A research conducted concluded 26 techniques for prompt engineering to boost response efficacy by at least 60%. 
        Those techniques have all been hereby implemented in our prompt engineering.
    """
    prompt = f"I am applying for a job of {context}. The audience is a recrutier expert in the field of {context}. Your task is to modify my given description to create a clear, brief and goal-oriented text paragraph for the specified purpose which is phrased clearly using ATS-friendly and recruiter-friendly language. Use natural human-like language. Do not use AI-sounding words. Do not use these words- 'beacon', 'leveraging', 'robust'. Include {context} related jargon and clad it with industry-specific keywords that recruiters and ATS look for, such as but not limited to {keywords} only wherever applicable. I am going to tip $9999 for a better solution. Don't use any formatting."

    # Leadership Experience modification
    if type == "lex":
        prompt = prompt + "This is my leadership experience. The purpose is to describe how I demonstrated leadership in this experience: " 

    # Work Experience modification
    if type == "wex":
        prompt = prompt + "This are my achievements in this job experience. The purpose is to hihglight my achievements in this role: "
    
    # Project Description modification
    if type == "proj":
        prompt = prompt + "This is my project description. The purpose is to describe my project and learnings: "
    """
        Additionally we can add to this prompt a few examples of how the respective dsecriptions from widely accepted resumes look like 
        to give an exaple to the LLM. This data is widely available online.
    """

    prompt = prompt + description + "\nAlso spell-check it and fix any grammatical errors. Do not over exaggerate the descriptions. I will charge a huge penalty if my instructions are not followed"
    return model.generate_content(prompt).text

if __name__ == '__main__':
    print(modify_des("say hi"))
 
