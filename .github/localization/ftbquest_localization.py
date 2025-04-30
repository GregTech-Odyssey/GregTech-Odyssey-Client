import json
import os
from pathlib import Path

import ftb_snbt_lib as snbt
from ftb_snbt_lib.tag import Compound, List, String

QUEST_PATH = Path('config/ftbquests/quests')

QUEST_LOCALIZED_PATH = Path('.github/localization/localized_quests')
QUEST_LOCALIZED_PATH.mkdir(exist_ok=True)

LANG_FILE_PATH = Path('config/openloader/resources/quests/assets/gto/lang')
os.makedirs(LANG_FILE_PATH, exist_ok=True)
SOURCE_LANGUAGE = 'zh_cn'

PACK_SHORT_KEY = "gto"
SOURCE_KEYS = {}

ESCAPE_SUBS = {
    r'%': r'%%',
    r'"': r'\"'
}


def escape_string(text: str) -> str:
    for match, req in ESCAPE_SUBS.items():
        text = text.replace(match, req)
    return text


def text_filter(text: str) -> bool:
    if not text:
        return False
    if text.startswith("{") and text.endswith("}"):
        return False
    if text.startswith("[") and text.endswith("]"):
        return False
    return True


def convert(file_path: Path) -> Compound:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = snbt.load(f)

    chapter = file_path.stem

    _convert(data, f'{PACK_SHORT_KEY}.{chapter}')
    return data


def _convert(data: Compound, lang_key: str):
    for key in filter(lambda x: data[x], data):
        if isinstance(data[key], Compound):
            _convert(data[key], f'{lang_key}.{key}')
        elif isinstance(data[key], List) and issubclass(data[key].subtype, Compound):
            for index in range(len(data[key])):
                tag = data[key][index]
                if 'id' in tag:
                    lk = f'{key}.{tag["id"]}'
                else:
                    lk = f'{key}{index}'
                _convert(tag, f'{lang_key}.{lk}')
        elif key in ['title', 'subtitle', 'description']:
            if isinstance(data[key], String) and text_filter(data[key]):
                lk = f'{lang_key}.{key}'
                SOURCE_KEYS[lk] = escape_string(data[key])
                data[key] = snbt.String(f'{{{lk}}}')
            elif isinstance(data[key], List) and issubclass(data[key].subtype, String):
                for index, i in enumerate(filter(lambda x: text_filter(data[key][x]), range(len(data[key])))):
                    lk = f'{lang_key}.{key}{index}'
                    SOURCE_KEYS[lk] = escape_string(data[key][i])
                    data[key][i] = snbt.String(f'{{{lk}}}')


def main():
    for file in os.listdir(QUEST_PATH):
        if file.endswith('.snbt'):
            localized_data = convert(QUEST_PATH / file)
            with open(QUEST_LOCALIZED_PATH / file, 'w', encoding='utf-8') as f:
                snbt.dump(localized_data, f)

    with open(LANG_FILE_PATH / f'{SOURCE_LANGUAGE}.json', 'w', encoding='utf-8') as f:
        json.dump(dict(sorted(SOURCE_KEYS.items())), f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
