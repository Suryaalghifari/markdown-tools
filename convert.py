from pathlib import Path
from markitdown import MarkItDown


BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
MD_DIR = BASE_DIR / "md"


def ensure_folders():
    DOCS_DIR.mkdir(exist_ok=True)
    MD_DIR.mkdir(exist_ok=True)


def list_files():
    files = sorted([
        file for file in DOCS_DIR.iterdir()
        if file.is_file()
    ])

    if not files:
        print("\nBelum ada file di folder docs/")
        print("Taruh file PDF/DOCX/PPTX/XLSX/HTML di folder docs/ dulu.\n")
        return []

    print("\nFile yang tersedia di docs/:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")

    return files


def convert_one_file():
    files = list_files()
    if not files:
        return

    try:
        choice = int(input("\nPilih nomor file: "))
        selected_file = files[choice - 1]
    except (ValueError, IndexError):
        print("\nPilihan tidak valid.\n")
        return

    output_file = MD_DIR / f"{selected_file.stem}.md"

    print(f"\nMengonversi: {selected_file.name}")
    print(f"Hasil ke: md/{output_file.name}")

    md = MarkItDown()
    result = md.convert(str(selected_file))

    output_file.write_text(result.text_content, encoding="utf-8")

    print("\nSelesai.\n")


def convert_all_files():
    files = list_files()
    if not files:
        return

    md = MarkItDown()

    for file in files:
        output_file = MD_DIR / f"{file.stem}.md"

        print(f"\nMengonversi: {file.name}")
        result = md.convert(str(file))
        output_file.write_text(result.text_content, encoding="utf-8")
        print(f"Hasil: md/{output_file.name}")

    print("\nSemua file selesai dikonversi.\n")


def main_menu():
    ensure_folders()

    while True:
        print("=== MarkItDown Converter ===")
        print("1. Lihat file di docs/")
        print("2. Convert satu file")
        print("3. Convert semua file")
        print("4. Keluar")

        choice = input("\nPilih menu: ").strip()

        if choice == "1":
            list_files()
        elif choice == "2":
            convert_one_file()
        elif choice == "3":
            convert_all_files()
        elif choice == "4":
            print("\nKeluar.\n")
            break
        else:
            print("\nMenu tidak valid.\n")


if __name__ == "__main__":
    main_menu()
