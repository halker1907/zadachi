def is_reversed(word: str) -> bool:
	return word == word[ ::-1]



assert is_reversed("топот") == True
assert is_reversed("топор") == False
assert is_reversed("") == True