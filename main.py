import re
from googletrans import Translator

translator = Translator()
dest_lang = "zh-cn"  # use "en" for english, "zh-cn" for simlified chinese

with open("input.xlf") as f:
    original = f.read().replace("\n", "")

translated = original  # make base of output text

source_tag_list = re.findall(r"<source>.+?</source>", original)

for source_tag in source_tag_list:
    target_tag = source_tag.replace("<source>", "<target>").replace(
        "</source>", "</target>"
    )  # make base of target_tag
    source_text_list = re.findall(r">(.+?)<", source_tag)
    for source_text in source_text_list:
        source_text = source_text.replace(" ", "")
        if source_text != "":
            print("translate {}".format(source_text))
            translated_text = translator.translate(
                source_text, src="ja", dest=dest_lang
            ).text
            target_tag = target_tag.replace(source_text, translated_text)
    translated = translated.replace(source_tag, source_tag + target_tag)

with open("output.xlf", mode="w") as f:
    f.write(translated)