def encode(words,key):
  newWord=""
  for ch in words:
    result = ord(ch)+key
    if result>ord('z'):
    newWord = newWord + chr(result)
  return newWord

def decode(words,key):
  newWord=""
  for ch in words:
    newWord = newWord + chr(ord(ch)-key)
  return newWord

print(encode("Zzzz",5))
print(decode("Mjqqt",5))