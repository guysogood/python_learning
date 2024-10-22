import random
import my_module

random_int = random.randint(1,10) #1-10
random_float = random.random() #0.0 - <1.0
random_uni = random.uniform(1,10) #1.0-10.0
print(random_int)
print(random_float)
print(random_uni)

print(my_module.my_fav_num)

words = ["Heads", "Tails"]
random_words = random.choice(words)
print(random_words)