async def update_check(change):
    my_file = open("./info/update.txt", "r")
    update = my_file.read()
    my_file.close()
    if change:
        update = "True" if update == "False" else "False"
        my_file = open("./info/update.txt", "w")
        my_file.write(f'{update}')
        my_file.close()
    return update