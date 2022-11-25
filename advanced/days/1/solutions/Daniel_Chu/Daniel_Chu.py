file_name = "Day1"
author = "Daniel Chu, Daniel Joseph, Alex Waneis, Dino Efstathiou, Hagop Khoshafian"
email = "chud002@tcdsb.ca"


Password = "jh0g45j0jfgm40fghy7ut03d20fhn0gf400057q0wd12vcx4089pyi231400gjh0"

Numbers = []

def numbers(input):
  if input == "1" or input == "2" or input == "3" \
  or input == "4" or input == "5" or input == "6" \
  or input == "7" or input == "9": 

    return True
  
for character in Password:
  if numbers(character):
    Numbers.append(character)

Numbers.sort(reverse = True)
for i in Numbers:
  print(i, end="")
