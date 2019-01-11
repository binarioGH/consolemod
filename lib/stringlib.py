#-*-coding: utf-8-*-
def editstring(string, index, instead):
	newstring = list(string)
	newstring[index] = str(instead)
	return ''.join(newstring)
def wordsearcher(string, *words):
	checklist = {}
	for word in words:
		if word in string:
			checklist[word] = (True, (string.find(word), string[::-1].find(word[::-1])))
		else:
			checklist[word] = (False)
	return checklist