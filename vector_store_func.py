from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_chroma import Chroma
from langchain_cohere import CohereEmbeddings
import re



embedding_model = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key="iiYtqoN8hTQ2EcoeV6FyeOqkT6wdvjFurq39gqMm")

def load_store_csv(path:str):
    store_csv_loader = CSVLoader(file_path=path,encoding="utf-8")
    store_data = store_csv_loader.load()
    return store_data

def create_store_database(data:list, path:str):
    vector_store=Chroma.from_documents(documents=data[:41], embedding=embedding_model, persist_directory=path)

def load_store_database(path:str):
    store_database = Chroma(persist_directory=path, embedding_function=embedding_model)
    return store_database

def extract_store_context(store_database:Chroma, message:str):
    documents_list = store_database.similarity_search(message)
    list_of_extracted_document_strings=[]

    for document in documents_list:
        page_content = document.page_content

        name = re.search(r"Name: (.+)", page_content).group(1)
        price = re.search(r"Price: (\d+)", page_content).group(1)
        discounted_price = re.search(r"DiscountedPrice: (\d+)", page_content).group(1)
        category = re.search(r"Category: (.+)", page_content).group(1)
        subcategory = re.search(r"SubCategory: (.+)", page_content).group(1)
        description = re.search(r"Description: (.+)", page_content).group(1)
        

        extracted_document_string = f"Name: {name}\nPrice: {price}\nDiscountedPrice: {discounted_price}\nCategory: {category}\nSubCategory: {subcategory}\nDescription: {description}"
        list_of_extracted_document_strings.append(extracted_document_string)

    return list_of_extracted_document_strings

    


