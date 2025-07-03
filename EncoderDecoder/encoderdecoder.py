import random
'''encoder decoder'''

user_input = input("enter the sentence to be encoded or decoded: ")
user_list = user_input.split(" ")
wtd = input("do you want to encode(E) or decode(D) ")

encoded = []
decoded = []

alpha_list = []
for i in range(97, 123):
  alpha_list.append(chr(i))


def encode_1(user_input):
  for i in user_list:
    if len(i) <= 3:
      encoded.append(i[::-1])
    else:
      random_letters1 = random.choices(alpha_list, k=3)
      random_letters2 = random.choices(alpha_list, k=3)
      encoded.append("".join(random_letters1) + i[1:len(i)] + i[0] +
                     "".join(random_letters2))
  print(" ".join(encoded))


def decode_1(user_input):
  for i in user_list:
    if len(i) <= 3:
      decoded.append(i[::-1])
    else:
      decoded.append(i[-4] + i[3:len(i) - 4])
  print(" ".join(decoded))


if wtd == "E":
  encode_1(user_input)

if wtd == "D":
  decode_1(user_input)
