from pathlib import Path
import json

DATA_PATH = Path(__file__).parent / "data"
root_text_fn = DATA_PATH / "input" / "root_2.txt"
root_json_fn = DATA_PATH / "output" / "root_verses.json"


def parse(root_text):
    verses = []
    for line in root_text.splitlines():
        if not line: continue
        verse = line[line.find("༽")+1:].strip()
        verse_lines = verse.split("། །")
        verse_lines = [l.strip() + "།" for l in verse_lines if l]
        verses.append(verse_lines)
    return verses

if __name__ == "__main__":
    root_text = root_text_fn.read_text()
    root_verses = parse(root_text)
    json.dump(root_verses, root_json_fn.open("w"), ensure_ascii=False, indent=2)
