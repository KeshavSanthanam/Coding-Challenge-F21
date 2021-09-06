# Coding-Challenge-F21
# By Keshav Santhanam
# Class of 2025
# 3 September 2021

# keywords for determining sentiment
positive = ["good", "calmly", "excellent", "wisdom", "serenity", "truth", "like", "draw", "ingenious", "prettily", "skilled", "pleasing", "agreeable", "respect", "sensible", "convenience", "delicate", "better"]
negative = ["bad", "furious", "rage", "yelled", "no", "cried", "exclaimed", "don't", "slippery", "watch", "fireman", "devil", "torrent", "unhappy"]
amplify = ["!", "very", "quickly", "fast", "more", "power", "spring", "capital", "extremely"]
calm_down = ["somewhat", "little", "indifferent", "observant"]

# read in file; convert to lowercase text for consistency with provided keywords
file = open("input.txt", "r")
line = file.read()
line = line.lower()
print("\nInput file read; string initialized... \n")

def find_sent(to_read):
    # initialize initial score and default multiplier (1)
    score = 0
    m = 1
    # calculate score based off keywords
    for x in amplify:
        if x in to_read:
            m = 2
    for x in calm_down:
        if x in to_read:
            m = 0.5
    for x in positive:
        if x in to_read:
            score += 1*m
            m = 1
    for x in negative:
        if x in to_read:
            score -= 1*m
            m = 1
    return score

# display final score for the entire input
direction = ""
if (find_sent(line) > 0):
    direction = "positive"
if (find_sent(line) == 0):
    direction = "neutral"
if (find_sent(line) < 0):
    direction = "negative"
print("The final score is:: ", find_sent(line), "(", direction, ")")

# repeating above steps for individual sentences
print("\nParsing individual sentences...\n")
sentences = line.split(".")
prev_end = 0
out_index = 0
for num in range(len(sentences)):
    out_index += 1
    a = sentences[num]
    print("The score for sentence ", out_index, " is:: ", find_sent(a))

print("\nClosing file...")
file.close()
print("\nEnd program.")