class FileManager:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def read_file(self):
        with open(self.nazwa, "r") as f:
            text = f.read()
            return text

    def update_file(self, new_text):
        with open(self.nazwa, "a") as f:
            f.write(new_text + "\n")
