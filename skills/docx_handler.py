from pathlib import Path


def build_output_filename(input_file, suffix='_translated'):
    path = Path(input_file)
    return str(path.with_name(f'{path.stem}{suffix}{path.suffix}'))


def validate_docx(file_path):
    return Path(file_path).exists() and file_path.lower().endswith('.docx')
