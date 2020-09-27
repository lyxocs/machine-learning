import os
def recursive_listdir(path):

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            print(file)

        elif os.path.isdir(file_path):
          recursive_listdir(file_path)

recursive_listdir('./LAB3/test-mails')