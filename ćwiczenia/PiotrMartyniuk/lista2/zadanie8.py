class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, "r") as f:
            content = f.read()
            return content

    def update_file(self, text_data):
        with open(self.file_name, "a") as f:
            f.write(text_data + "\n")