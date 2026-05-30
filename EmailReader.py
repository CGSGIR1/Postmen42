from Email import Email


class EmailReader:
    KEY_WORDS = {
        "subject": "subject", "тема": "subject", "tema": "subject",
        "from": "from", "от кого": "from", "ot kogo": "from",
        "to": "to", "кому": "to", "komu": "to",
        "date": "date", "дата": "date", "data": "date",
    }
    def read(self, file_path):
        print(self.KEY_WORDS["от кого"])
        try:
            subject = ""
            recipient = ""
            source_path = file_path
            body = ""
            with open(file_path, 'r') as file:
                for line in file:
                    if ":" in line:
                        component = line[:line.index(":")].strip()
                        if self.KEY_WORDS[component.lower()] == "subject":
                            subject = line[line.index(":")+1:].strip()
                        elif self.KEY_WORDS[component.lower()] == "from":
                            pass
                        elif self.KEY_WORDS[component.lower()] == "to":
                            recipient = line[line.index(":")+1:].strip()
                        elif self.KEY_WORDS[component.lower()] == "date":
                            pass
                        else:
                            raise ValueError("Непредвиденный заголовок письма: " + component.lower())
                    else:
                        body = line + file.read()
            return Email(recipient, subject, body, source_path)
        except ValueError as e:
            print(e)
        except FileNotFoundError as e:
            print("Ошибка чтения файла: такого файла не существует")
        except Exception as e:
            print("Ошибка чтения файла")