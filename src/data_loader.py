from pathlib import Path
from typing import List,Any
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, CSVLoader, Docx2txtLoader, JSONLoader, SQLDatabaseLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader

def load_all_documents(data_dir: str)-> List[Any]:
    data_path = Path(data_dir).resolve()
    print(f"[Debug] data path: {data_path}")
    documents = []
    #PDF files
    pdf_files = list(data_path.glob("**/*.pdf"))
    if len(pdf_files)>0:
        print(f"{len(pdf_files)} files found: {[str(f) for f in pdf_files]}")
        for pdf_file in pdf_files:
            print(f"Loading pdf file: {pdf_file}")
            try:
                loaded = PyMuPDFLoader(str(pdf_file)).load()
                documents.extend(loaded)

            except Exception as e:
                print(f" Error loading pdf files {pdf_file}: {e}")
    
    #Text File
    text_files = list(data_path.glob("**/*.txt"))
    if len(text_files)>0:
        print(f"{len(text_files)} files found: {[str(f) for f in text_files]}")
        for text_file in text_files:
            print(f"Loading txt file: {text_file}")
            try:
                documents.extend(TextLoader(str(text_file)).load())
            except Exception as e:
                print(f" Error loading txt files {text_file}: {e}")
    
    #csv File
    csv_files = list(data_path.glob("**/*.csv"))
    if len(csv_files)>0:
        print(f"{len(csv_files)} files found: {[str(f) for f in csv_files]}")
        for csv_file in csv_files:
            print(f"Loading csv file: {csv_file}")
            try:
                documents.extend(CSVLoader(str(csv_file)).load())
            except Exception as e:
                print(f" Error loading txt files {csv_file}: {e}")

    #sql File
    sql_files = list(data_path.glob("**/*.sql"))
    if len(sql_files)>0:
        print(f"{len(sql_files)} files found: {[str(f) for f in sql_files]}")
        for sql_file in sql_files:
            print(f"Loading sql file: {sql_file}")
            try:
                documents.extend(SQLDatabaseLoader(str(sql_file)).load())
            except Exception as e:
                print(f" Error loading sql files {sql_file}: {e}")

    #json File
    json_files = list(data_path.glob("**/*.json"))
    if len(json_files)>0:
        print(f"{len(json_files)} files found: {[str(f) for f in json_files]}")
        for json_file in json_files:
            print(f"Loading json file: {json_file}")
            try:
                documents.extend(JSONLoader(str(json_file)).load())
            except Exception as e:
                print(f" Error loading json files {json_file}: {e}")


    return documents

