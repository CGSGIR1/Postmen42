from pathlib import Path
import shutil

class FileMover:
    def __init__(self):
        if Path("output").exists():
            shutil.rmtree(Path("output"))

    def move_files(self, email, category):
        folder = Path("output") / category
        folder.mkdir(parents=True, exist_ok=True)
        src = Path(email.source_path)
        dst = folder / src.name
        try:
            shutil.copy2(src, dst)
        except FileNotFoundError as e:
            print("Ошибка директории")
            print(e)
        except PermissionError as e:
            print("Ошибка прав программы")
            print(e)
        except Exception as e:
            print(e)