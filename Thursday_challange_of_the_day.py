word = str(input("type a word: "))

vowels=0

for i in word:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels = vowels + 1

print(vowels)