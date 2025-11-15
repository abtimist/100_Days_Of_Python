def calculate_love_score(name1,name2):
  word_list=["true","love"]
  name1=name1.lower()
  name2=name2.lower()
  trueCount=0
  loveCount=0
  for letter in name1:
      if letter in word_list[0]:
          trueCount+=1
      if letter in word_list[1]:
          loveCount+=1
  for letter in name2:
      if letter in word_list[0]:
          trueCount+=1
      if letter in word_list[1]:
          loveCount+=1
  print(str(trueCount)+str(loveCount))
name1=input("Enter first person's full name: ")
name2=input("Enter second person's full name: ")
calculate_love_score(name1,name2)
