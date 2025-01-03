import os
from secret_key import gemini_key
from langchain_google_genai import ChatGoogleGenerativeAI
from embeding import similarity_result
from google.cloud import aiplatform
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


os.environ["GOOGLE_API_KEY"] = gemini_key
#os.environ['OPENAI_API_KEY'] = openapi_key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,    
    # other params...
)


prompt_template_fromdoc = PromptTemplate(
    input_variables =['resonse'],
    template = "generate good response for ,{resonse}"
)
prompt_template_fromllm = PromptTemplate(
    input_variables =['resonse'],
    template = "try creative answer with ,{resonse}"
)

chat_message=input('messaage: ')
result=similarity_result(chat_message)
p1 = prompt_template_fromdoc.format(resonse=result)
p2 = prompt_template_fromllm.format(resonse=chat_message)


llm_chain_fromdoc = LLMChain(llm=llm, prompt=prompt_template_fromdoc)
llm_chain_= LLMChain(llm=llm, prompt=prompt_template_fromllm)

from langchain.chains import SimpleSequentialChain
chain = SimpleSequentialChain(chains = [llm_chain_, llm_chain_fromdoc])

content = chain.invoke(chat_message)

print(content)




