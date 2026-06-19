import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    dir_path = os.path.dirname(destination)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source, "r") as file_in:
        content = file_in.read()

    with open(destination, "w") as file_out:
        file_out.write(content)

    os.remove(source)
