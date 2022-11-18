import logging
from deep_translator import GoogleTranslator, LingueeTranslator, PonsTranslator
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--file_path",
    type=str,
    help="Path to English .txt file to be translated to German.",
)

def translate_file(path):
    file = open(path, 'r')
    translations = ''
    for line in file:
        line = line.strip()
        print(line)
        try:
            translated = LingueeTranslator(source="en", target="de").translate(line)
        except:
            try:
                translated = GoogleTranslator(source="en", target="de").translate(line)
            except:
                try:
                    translated = PonsTranslator(source="en", target="de").translate(line)
                except:
                    translated = line
                    logging.warning(f'{line} not translated')
        translations = translations + translated + '\n'
    file.close()
    out = open(path.split('.')[0]+'-de.txt', "w")
    out.write(translations)
    out.close()



if __name__ == "__main__":
    args = parser.parse_args()
    print(args.file_path)
    translate_file(args.file_path)