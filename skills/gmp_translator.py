GMP_TERMS = {
    'stoppering': 'укупоривание',
    'stopper': 'пробка',
    'batch record': 'протокол серии',
    'deviation': 'отклонение',
    'change control': 'управление изменениями',
    'corrective action': 'корректирующее действие',
    'preventive action': 'предупреждающее действие',
    'qualification': 'квалификация',
    'validation': 'валидация'
}


def apply_gmp_terms(text: str) -> str:
    result = text
    for source, target in GMP_TERMS.items():
        result = result.replace(source, target)
        result = result.replace(source.title(), target)
    return result


def translate_gmp_text(translated_text: str) -> str:
    return apply_gmp_terms(translated_text)
