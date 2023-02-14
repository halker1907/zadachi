def test(word_1:str, word_2:str) -> bool:
	if len(word_1) != len(word_2):
		return False

	for letter in word_1:
		if not letter in word_2:
			return False
	return True

	

assert test("дуб", "буд") == True
assert test("дуб", "бут") == False
assert test("", "дуб") == False
assert test("","") == True
assert test("дуб","дубб") == False
assert test("дуб","ду") == False
