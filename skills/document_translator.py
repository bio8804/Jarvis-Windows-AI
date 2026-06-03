from docx import Document
from ai.chat_memory import ChatMemory
from skills.gmp_translator import translate_gmp_text


class DocumentTranslator:
    def __init__(self, provider='deepseek'):
        self.memory = ChatMemory(provider=provider)

    def translate_docx(self, input_file, output_file):
        doc = Document(input_file)

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()

            if not text:
                continue

            translated = self.memory.ask(
                f'Translate the following pharmaceutical/GMP text into Russian and preserve meaning and formatting: {text}'
            )

            paragraph.text = translate_gmp_text(translated)

        doc.save(output_file)
        return output_file
