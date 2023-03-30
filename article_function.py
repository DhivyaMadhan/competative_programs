import os
import re
import json
import pymongo

mongodb_connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


def mongodb_method(input_data, flag):
    if flag == 0:
        try:
            global database
            database = mongodb_connection[input_data]
            return True
        except Exception as error:
            print(f"Error while creating database: {error}")
            return False
    elif flag == 1:
        try:
            global collection
            collection = database[input_data]
            return True
        except Exception as error:
            print(f"Error while creating collection: {error}")
            return False
    else:
        try:
            print(collection.insert_one(input_data).inserted_id)
        except Exception as error:
            print(f"Error while inserting document: {error}")


def text_parser(text_data):
    regex_output = re.findall(r"""(.*?\.)""", text_data)
    return regex_output


def files_in_folder(path, article):
    # print(article)
    if mongodb_method(path.split("\\")[-1], 0):
        for each_file in article:
            if mongodb_method(each_file, 1):
                print(path + "\\" + each_file)
                with open(path + "\\" + each_file, "r", encoding='utf-8') as each_article:
                    result = text_parser(each_article.read())
                    # print(result)
                    for index, value in enumerate(result):
                        # print(int(index)+1, len(value.split()), value)
                        dict_value = {"folder name": path.split("\\")[-1], "file name": each_file,
                                          "line number": int(index) + 1,
                                      "number of words": len(value.split()), "Text": value}
                        # print("dict_value", dict_value)
                        print("json", json.dumps(dict_value))
                        mongodb_method(dict_value, 2)
