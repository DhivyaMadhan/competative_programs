import os
import article_configuration as configuration
import article_function

path = configuration.folder_path
list_dir = os.listdir(path)
article_function.files_in_folder(path, list_dir)

