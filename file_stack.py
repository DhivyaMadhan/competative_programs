import os
import file_stack_configuration as configuration
path = os.getcwd() + "\\" + configuration.filename
is_exist = os.path.exists(path)
if not is_exist:
    os.mkdir(configuration.filename)
    os.chdir(path)
    print(f"successfully created a folder name:{configuration.filename}")
for iterate in range(1, 11):
    folder_name = f"temp{iterate}"
    # print("temp"+str(iterate))
    # print(f"temp{iterate}")
    os.mkdir(folder_name)
    for iterate1 in range(1, 11):
        # os.mkdir(folder_name+r"\sub_temp"+str(iterate1))
        os.mkdir(f"{folder_name}\\sub_temp{iterate1}")
        for iterate2 in range(1, 11):
            file = open(f"{folder_name}\\sub_temp{iterate1}\\file{iterate2}.txt", "w")
            output_line = [f"file name: file{iterate2}.txt\n", f"sub parent dir: sub_temp{iterate1}.txt\n",
                           f"parent dir: temp{iterate}.txt"]
            file.writelines(output_line)
            file.close()
            file = open(f"{folder_name}\\sub_temp{iterate1}\\file{iterate2}.txt", "a")
            output_line = f"\nfile name: file{iterate2}.txt\nsub parent dir: sub_temp{iterate1}.txt\nparent dir: " \
                          f"temp{iterate}.txt"
            file.write(output_line)
            file.close()
