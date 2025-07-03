import random

guess = [
    "Elephant", "Mysterious", "Adventure", "Chocolate", "Galaxy", "Umbrella",
    "Journey", "Penguin", "Vibrant", "Marshmallow", "Quarantine", "Whisper",
    "Pomegranate", "Thunderstorm", "Knowledge", "Paradox", "Serendipity",
    "Architect", "Trampoline", "Lantern", "Cryptic", "Eclipse", "Nostalgia",
    "Rhythmic", "Lullaby"
]

history = []
my_word = random.choice(guess).lower()
my_list = list(my_word)
print(my_word)
empty_list = ["_"] * len(my_word)
attempt = len(my_word) + 10

while True:
  print(f"you have {attempt} choices left")
  user_input = input("enter a letter:")

  if user_input in history:
    print("you have already tried it you are not loosing attempts")
    continue
  else:
    if user_input.isalpha():
      attempt -= 1

      if attempt == 0:
        print("you lost")
        break

      if user_input in my_list:
        empty_list[my_list.index(user_input)] = user_input
        my_list[my_list.index(user_input)] = "_"
        print("".join(empty_list))
        if "".join(empty_list) == my_word:
          print("you won")
          break

      else:
        print("not found")
        history.append(user_input)

    else:
      print("enter a valid letter")
      continue
