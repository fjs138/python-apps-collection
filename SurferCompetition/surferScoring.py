# Line length limit should be 72 characters---------------------------->
# Split lines with \
# "Declaring" variables
firstPlace = 0
secondPlace = 0
thirdPlace = 0
scores=[]
# Open the results of the surfing contest, which are stored in a plaintext file


# Print the results to screen
# print(resultsTXT)


print("Opening the ./results.txt file...")
print()
print("Calculating and sorting scores...")
print()
resultsDotTxt = open("results.txt")
# shorter way of doing things; "for" with open("results.txt") inline
# for currentLine in open("results.txt"):
for currentLine in resultsDotTxt:
    (currentLineSurfer, currentLineScore) = currentLine.split()
    surferAndScore = [currentLineSurfer, currentLineScore]
    scores.append(float(currentLineScore))
# Better way, using array aka list
scores.sort()
scores.reverse()
# clean one line sort with reverse:
# scores.sort(reverse = True)
#print(scores)

# My way, not so good
#   if float(currentLineScore) > thirdPlace:
#       thirdPlace = secondPlace
#       secondPlace = firstPlace
#       firstPlace = float(currentLineScore)
firstPlace = scores[0]
secondPlace = scores[1]
thirdPlace = scores[2]
resultsDotTxt.close()
print("Closing the ./results.txt file...")
print()
print("First place score is: ")
print(firstPlace)
print("Second place score is: ")
print(secondPlace)
print("Third place score is: ")
print(thirdPlace)
print()
print("The top three scores are:")
print(scores[0:3])
