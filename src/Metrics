import argparse
import csv
from pathlib import Path
from collections import defaultdict


def load_true_labels(csv_path: str) -> dict:
    if not Path(csv_path).exists():
        print(f"Ошибка: файл {csv_path} не найден")
        return None
    true_labels = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row["filename"].strip()
            label = row["true_label"].strip()
            true_labels[filename] = label
    return true_labels


def load_predicted_labels(output_folder: str) -> dict:
    if not Path(output_folder).exists():
        print(f"Ошибка: папка {output_folder} не существует")
        return None
    predicted_labels = {}
    output_path = Path(output_folder)

    for category_folder in output_path.iterdir():
        if category_folder.is_dir():
            category_name = category_folder.name
            for file in  category_folder.iterdir():
                if file.is_file():
                    predicted_labels[file.name] = category_name

    return predicted_labels


def compute_metrics(true_labels: dict, predicted_labels: dict):
    all_categories = set(true_labels.values()) | set(predicted_labels.values())
    tp = defaultdict(int)
    fp = defaultdict(int)
    fn = defaultdict(int)

    correct = 0
    total = 0

    common_files = set(true_labels.keys()) & set(predicted_labels.keys())

    if not common_files:
        print("Нет совпадающих файлов между labels.csv и папкой output")
        print("Проверь что имена файлов в CSV совпадают с именами файлов в подпапках.")
        return None, None

    for filename in common_files:
        true = true_labels[filename]
        pred = predicted_labels[filename]
        total += 1

        if true == pred:
            correct += 1
            tp[true] += 1
        else:
            fp[pred] += 1
            fn[true] += 1  

    if total > 0:
        accuracy = correct / total
    else:
        accuracy = 0

    error_rate = 1 -accuracy

    overall = {
        "total": total,
        "correct": correct,
        "accuracy": accuracy,
        "error_rate": error_rate,
    }

    per_class = {}
    for cat in sorted(all_categories):
        t = tp[cat]
        f_pos = fp[cat]
        f_neg = fn[cat]

        if (t + f_pos) > 0:
            precision = t / (t + f_pos)
        else:
            precision = 0.0

        if (t + f_neg) > 0:
            recall = t / (t + f_neg)
        else:
            recall = 0.0

        if (precision + recall) > 0:
            f1 = (2 * precision * recall) / (precision + recall)
        else:
            f1 = 0.0

        per_class[cat] = {
            "tp": t,
            "fp": f_pos,
            "fn": f_neg,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

    return overall, per_class


def print_report(overall: dict, per_class: dict):
    print()
    print("Отчет по метрикам")
    print()
    print("Оценено ", overall['total'], " писем")
    print("Правильно:", overall['correct'])
    print()
    print("Accuracy:", format(overall['accuracy'], '.2%'))
    print("Error Rate:", format(overall['error_rate'], '.2%'))
    print()
    print(f"{'Категория':<12} {'Precision':>10} {'Recall':>8} {'F1':>8} {'TP':>5} {'FP':>5} {'FN':>5}")
    for cat, m in per_class.items():
        print(f"{cat:<12} {m['precision']:>9.2%} {m['recall']:>7.2%} {m['f1']:>7.2%} {m['tp']:>5} {m['fp']:>5} {m['fn']:>5}")

def main():
    parser = argparse.ArgumentParser(description="Метрики классификатора писем")
    parser.add_argument("--labels", default="labels.csv",help="CSV с правильными метками")
    parser.add_argument("--output", default="../output",help="Папка с разложенными классификатором письма")
    args = parser.parse_args()

    print(f"Читаем эталонные метки из: {args.labels}")
    true_labels = load_true_labels(args.labels)
    if true_labels is None:
        return
    print(f"Загружено {len(true_labels)} эталонов")

    print(f"Читаем предсказанные метки из папки: {args.output}")
    predicted_labels = load_predicted_labels(args.output)
    if predicted_labels is None:
        return
    print(f"Найдено {len(predicted_labels)} предсказанных меток")

    overall,per_class = compute_metrics(true_labels, predicted_labels)

    if overall is not None:
        print_report(overall, per_class)


if __name__ == "__main__":
    main()
