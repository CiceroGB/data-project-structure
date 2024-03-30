from etl.extract import extract_excel

if __name__ == "__main__":
    path = "data/input"
    data =  extract_excel(path)
    print(data)