#https://openhatch.org/wiki/Philadelphia_Python_Workshop

print 'Hello World!'

#basic math function
def add(x, y):
  return x + y

result = add(10, 20)
print result

#basic list
students = ["Amy", "Bob", "Sara", "Danny", "Ethan"]

#loop to check if a student's name has a vowel in it and print a statement
for student in students:
    # if the first letter of the string (student's name) is in the string "AEIOU"
    if student[0] in "AEIOU":
        print student + " starts with a vowel"

#loop to put students who start with vowel into a new list
student_vowels = []
#this empty list needs to be outside the for loop so the list isn't reset each time it loops

for student in students:
    if student[0] in "AEIOU":
        student_vowels.append(student)

print student_vowels


#embedded for loops:
letters = ["a", "b", "c"]
numbers = [1,2,3]

for letter in letters:
    for number in numbers:
        print letter * number


#basic while loop
i = 0
while i < 10:
    print i
    i = i + 1



#set an empty dictionary
mydict = {}
#add the keys and values
mydict["Julie"] = 20
mydict["Amy"] = 45

#run the keys function to get the keys in a list
mydict.keys()
#run the values function
mydict.values()

for friend in mydict.keys():
    print friend + " is " + str(mydict[friend])


