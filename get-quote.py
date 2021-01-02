import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1 
  rnd1 = random.randint(0,last)
  rnd2 = random.randint(0,last)
  str1 = quotes[rnd1].rstrip('\n')
  str2 = quotes[rnd2].rstrip('\n')

  
  print(str1,str2)

  str3 = input()
  str3 = str3 + '\n'
  
  
  with open("quotes.txt", "a") as a_writer:
    a_writer.write(str3)

if __name__== "__main__":
  primary()
