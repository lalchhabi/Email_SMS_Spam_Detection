import chardet
with open("spam.csv", "rb") as f:
    result = chardet.detect(f.read())
print(result)  # This will show the file's encoding
