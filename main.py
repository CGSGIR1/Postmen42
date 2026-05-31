from EmailReader import EmailReader
from Classifier import Classifier
from FileMover import FileMover
if __name__ == "__main__":
    t1 = EmailReader()
    c1 = Classifier()
    f1 = FileMover()
    for i in range(1, 110):
        try:
            path = "inbox/mail_" + "0" * (4 - len(str(i))) + str(i) + ".txt"
            print(path)
            em = t1.read(path)
        except Exception as e:
            print(e)
        else:
            print("New email: " + str(i))
            print("SUB: " + em.subject)
            print("REC: " + em.recipient)
            print("BOD: " + em.body[:20].strip())
            cat = c1.classify(em)
            print("CAT: " + cat)
            f1.move_files(em, cat)
        print("-----------------------")