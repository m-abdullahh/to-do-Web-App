FILEPATH = 'todos.txt'


def read_file(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        return file.readlines()


def write_file(tmp_list, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(tmp_list)
