from pathlib import Path
from markitdown import MarkItDown


BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
MD_DIR = BASE_DIR / "md"

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".xls",
    ".html",
    ".htm",
    ".txt",
    ".csv",
}


def ensure_folders():
    DOCS_DIR.mkdir(exist_ok=True)
    MD_DIR.mkdir(exist_ok=True)


def get_supported_files():
    files = []

    for file in DOCS_DIR.iterdir():
        if not file.is_file():
            continue

        if file.name == ".gitkeep":
            continue

        if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        files.append(file)

    return sorted(files)


def list_files():
    files = get_supported_files()

    if not files:
        print("\nBelum ada file yang didukung di folder docs/.")
        print("Taruh file PDF, DOCX, PPTX, XLSX, HTML, TXT, atau CSV ke folder docs/.\n")
        return []

    print("\nFile yang tersedia di docs/:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")

    return files


def convert_file(file, md_converter):
    output_file = MD_DIR / f"{file.stem}.md"

    print(f"\nMengonversi: {file.name}")
    print(f"Hasil ke: md/{output_file.name}")

    try:
        result = md_converter.convert(str(file))
        output_file.write_text(result.text_content, encoding="utf-8")
        print("Status: berhasil")
    except Exception as error:
        print(f"Status: gagal")
        print(f"Error: {error}")


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

    md_converter = MarkItDown()
    convert_file(selected_file, md_converter)

    print("\nSelesai.\n")


def convert_all_files():
    files = list_files()
    if not files:
        return

    print(f"\nTotal file yang akan dikonversi: {len(files)}")

    md_converter = MarkItDown()

    for file in files:
        convert_file(file, md_converter)

    print("\nBulk convert selesai.\n")


def main_menu():
    ensure_folders()

    while True:
        print("=== Markdown Tools ===")
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