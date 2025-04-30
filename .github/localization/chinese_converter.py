import json
import os
from pathlib import Path

INPUT_FILE_PATH = Path('config/openloader/resources/quests/assets/gto/lang/zh_cn.json')
OUTPUT_FILE_PATH = Path('config/openloader/resources/quests/assets/gto/lang/zh_tw.json')

mapping_table = {}

def load_mapping_table():
    with open(Path('.github/localization/SimplifiedToTraditional.properties'), 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and '=' in line:
                key, value = line.split('=')
                key_char = key.encode('utf-8').decode('unicode_escape')
                value_char = value.encode('utf-8').decode('unicode_escape')
                mapping_table[key_char] = value_char


def convert(text):
    output_text_builder = []
    for character in text:
        converted_char = mapping_table.get(character, character)
        output_text_builder.append(converted_char)
    return ''.join(output_text_builder)


def convert_json(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    def recursive_convert(obj):
        if isinstance(obj, str):
            return convert(obj)
        elif isinstance(obj, list):
            return [recursive_convert(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: recursive_convert(value) for key, value in obj.items()}
        else:
            return obj

    converted_data = recursive_convert(data)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(converted_data, file, ensure_ascii=False, indent=4)


load_mapping_table()

if __name__ == "__main__":
    if not os.path.exists(os.path.dirname(OUTPUT_FILE_PATH)):
        os.makedirs(os.path.dirname(OUTPUT_FILE_PATH))

    convert_json(INPUT_FILE_PATH, OUTPUT_FILE_PATH)
