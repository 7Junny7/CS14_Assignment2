name = input("Enter student name\t:\n")
try:
    exam_first = int(input("Enter first exam score\t:\n"))
except Exception:
# if type(exam_first) != int:
    print("\nTest score 1 is not valid, must be all digits.")
    print("Program stopped working.")
    exit()
if not(0 <= exam_first <= 100):
    print("\nTest score 1 is not valid, must be between 0 - 100 inclusive.")
    print("Program stopped working.")
    exit()
try:
    exam_second = int(input("Enter second exam score\t:\n"))
except Exception:
    print("\nTest score 2 is not valid, must be all digits.")
    print("Program stopped working.")
    exit()
if not(0 <= exam_second <= 100):
    print("\nTest score 2 is not valid, must be between 0 - 100 inclusive.")
    print("Program stopped working.")
    exit()
try:
    exam_third = int(input("Enter third exam score\t:\n"))
except Exception:
    print("\nTest score 3 is not valid, must be all digits.")
    print("Program stopped working.")
    exit()
if not(0 <= exam_third <= 100):
    print("\nTest score 3 is not valid, must be between 0 - 100 inclusive.")
    print("Program stopped working.")
    exit()
try:
    quiz = int(input("Enter quiz score\t:\n"))
except Exception:
    print("\nQuiz score is not valid, must be all digits.")
    print("Program stopped working.")
    exit()
if not(0 <= quiz <= 100):
    print("\nQuiz score is not valid, must be between 0 - 100 inclusive.")
    print("Program stopped working.")
    exit()
try:
    programming = int(input("Programming total\t:\n"))
except Exception:
    print("\nProgramming assignment score is not valid, must be all digits.")
    print("Program stopped working.")
    exit()
if not(0 <= programming <= 100):
    print("\nProgramming assignment score is not valid, must be between 0 - 100 inclusive.")
    print("Program stopped working.")
    exit()

average = (exam_first + exam_second + exam_third) / 3
avr_grade = (average * 0.6) + (quiz * 0.1) + (programming * 0.3)
if avr_grade >= 90:
    letter_grade = "A"
elif avr_grade >= 80:
    letter_grade = "B"
elif avr_grade >= 70:
    letter_grade = "C"
elif avr_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\nHello {:s}, here is your report:".format(name))
print("\t\t\tTest Scores:\t{:d}, {:d}, {:d}".format(exam_first,exam_second,exam_third))
print("\t\t\tTest Average:\t{:.2f}".format(average))
print("\t\t\tQuiz Score:\t{:d}".format(quiz))
print("\t\t\tProgramming Score:\t{:.2f}".format(programming))
print("\t\t\tGrade Average:\t{:.2f}".format(avr_grade))
print("\t\t\tLetter Grade:\t{:s}".format(letter_grade))
