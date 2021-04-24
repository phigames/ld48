import json

punct = [".","?","!",","]

with open("scores.txt") as s, open("alternatives.jsonl","w") as a:

	quote = []

	for line in s:
		
		dic = {}
		line = line.split("\t")
		original = line[0]
		suggestions = [sugg_score.split()[0] for sugg_score in line[1:]]

		if not any(character.isalnum() for character in original):
			suggestions = punct[:]

		if original in suggestions:
			suggestions.remove(original)

		if original.strip() == "</s>":
			print(json.dumps(quote))
			quote = []
			continue




		#dic[original] = suggestions
		dic["word"] = original
		dic["alternatives"] = suggestions

		quote.append(dic)



		
	#print(dic)
