#!/usr/bin/python3

import json

#with open("result_copy.json", "r") as f:
    #chat_history = json.load(f.read())

chat = json.load(open("result.json", "r", encoding="utf-8"))

words = {}

for message in chat["messages"]:
    if len(message["text_entities"]) > 0:
        for entity in message["text_entities"]:
            for word in entity["text"].strip().split(" "):
                word = word.lower()

                if word.startswith("http://") or word.startswith("https://"):
                    continue

                try:
                    prev = words[word]
                except KeyError:
                    words[word] = 0
                
                prev = words[word]

                words[word] = prev + 1

words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))

with open("words.json", "w", encoding="utf-8") as f:
    json.dump(words, f, indent=4, ensure_ascii=False)