import google.generativeai as genai
import os
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "2"

genai.configure(api_key="use you key here")

model = genai.GenerativeModel("gemini-2.5-flash")



while True:
    prompt = input("You: ")
    response = model.generate_content(prompt)
    if prompt=='quit':
        break
    txt = str(response.text)
    txt = txt.replace("*", "")

    print(f"AI:{txt.strip()}")
