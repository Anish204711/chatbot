import os
from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
from gensim.models import Word2Vec


#from dataprep import data_prep

# os.environ["GOOGLE_API_KEY"] = gemini_key
# #os.environ['OPENAI_API_KEY'] = openapi_key
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0,    
#     # other params...
# )
# with open("data/new_data.txt", "r", encoding="utf-8") as file:
#     text = file.read()

#data=data_prep()
#model2 = gensim.models.Word2Vec(data, min_count = 1, vector_size= 100, window = 5, sg = 1)
#model2.save("word2vec_model.model")

def similarity_result(text):
    text_list=text.split()
    result=[]
    data=[]
    model = Word2Vec.load("word2vec_model.model")
    for item in text_list:        
        try:
            result.append(model.wv.most_similar(item, topn=5))
        except:
            result.append(item)
    for item in result:
        for tup in item:
            data.append(tup[0])
    return data


# emb_model = genai.embed_content(
#         model="models/text-embedding-004",
#         content='good morning this is anish from gatthaghar .'
#         )
# emb_model_list=emb_model['embedding']

# persist_directory = 'data/chroma/'
# with open("emb.txt", "r", encoding="utf-8") as file:
#     text = file.read()
# #Create the vector store

# emb_model_list=['']
# emb_model_list[0]=text
# vectordb = Chroma.from_documents(
#     documents=documents,
#     embedding=emb_model_list,
#     persist_directory=persist_directory
# )
# print(vectordb._collection.count())

