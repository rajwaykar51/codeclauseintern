from difflib import SequenceMatcher
#Simple Plagiarism Checker
with open('1.txt') as file_1,open('2.txt') as file_2:
        file1 = file_1.read()
        file2 = file_2.read()

match = SequenceMatcher(None,file1,file2).ratio()

result= int(match*100)

print(f'Files are {result}% similar')