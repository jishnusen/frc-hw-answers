words = ["dog", "cat", "mouse", "elephant", "lion", "giraffe", "leopard", "fish", "bird"]

new_word = raw_input("Input a word: ")

if new_word in words:
  print "You word exists in the array!"
else:
  words.append(new_word)
  print "Your word was added to the array!"

print words