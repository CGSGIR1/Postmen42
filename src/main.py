import argparse
from pathlib import Path
from EmailReader import EmailReader
from Classifier import Classifier
from FileMover import FileMover
from Logger import Logger
import logging
log = logging.getLogger(__name__)
def main():
    parser = argparse.ArgumentParser(description="Сортировщик писем")
    parser.add_argument("--input", default="../inbox", help="папка с письмами")
    parser.add_argument("--output", default="../", help="путь для папки")
    parser.add_argument("--debug", action="store_true", help="режим debug")
    args = parser.parse_args()
    logger = Logger(args.debug)
    if not Path(args.input).exists():
        log.error(f"Директория {args.input} не найдена")
        return
    log.info(f"Директория input: {args.input}, директория output: {args.output}output")

    mover = FileMover(args.output)
    reader = EmailReader()
    classifier = Classifier()


    for path in Path(args.input).iterdir():
        if path.is_file():
            email = reader.read(path)
            category = classifier.classify(email)
            logger.email_log(email, category)
            mover.move_files(email, category)

    log.info(logger.result_report())

if __name__ == "__main__":
    main()