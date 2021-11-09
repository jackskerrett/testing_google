def extract_text(text, target):
    var = text.split(target)
    return var[1].split("\\")[0]
