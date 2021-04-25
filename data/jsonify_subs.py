import json

punct = [".", "?", "!", ","]

with open("../scores.txt") as s:  # , open("alternatives.jsonl", "w") as a:

    quote = []
    counter = 0

    for line in s:

        dic = {}
        line = line.split("\t")
        original = line[0]
        suggestions = [sugg_score.split()[0] for sugg_score in line[1:]]

        for s in suggestions:
            if s in punct:
                suggestions.remove(s)

        if not any(character.isalnum() for character in original):
            suggestions = punct[:]

        if original in suggestions:
            suggestions.remove(original)

        if "</s>" in suggestions:
            suggestions.remove("</s>")

        if original.strip() == "</s>":
            if counter <= 140:
                print(json.dumps(quote))
            quote = []
            counter = 0
            continue

        counter += len(original) + 1

        # dic[original] = suggestions
        dic["word"] = original
        dic["alternatives"] = suggestions

        quote.append(dic)

    # print(dic)
