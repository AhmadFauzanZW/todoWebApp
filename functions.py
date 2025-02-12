def imporData(filepath):
    """
    Fungsi ini akan membuka text file 'filepath' dan akan
    mengambil data Todo List yang akan digunakan pada program
    :return:
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def eksporData(filepath, todos):
    """
    Fungsi ini akan membuka text file 'filepath'
    kemudian menyimpan data Todo List dari program ke
    text file tersebut
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)

def tampilkanTodoList(todos):
    """
    Sesederhana namanya, fungsi ini akan menampilkan Todo List
    dari list item
    :param todos: List of todos
    :return:
    """
    for i, item in enumerate(todos, start=1):
        item = item.strip("\n")
        print(f"{i}. {item}")

def konfirmasi(pilihan, todos, urutan_list):
    """
    Fungsi ini akan memproses pilihan yang di input oleh user
    dalam konteks Ya / Tidak sebagai konfirmasi
    :param pilihan:
    :param todos: List of todos
    :param urutan_list: Index of the todo to remove
    :return:
    """
    if pilihan == "Y":
        todos.pop(urutan_list)
        print("\nSelamat! anda telah menyelesaikan 1 rencana anda :)")
    elif pilihan == "T":
        print("\nSelamat berjuang untuk menyelesaikan rencana anda!")
    else:
        print("\nPilihan anda tidak valid! kembali ke menu utama")