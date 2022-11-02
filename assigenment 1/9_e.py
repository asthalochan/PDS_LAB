import random
import string
s=string.ascii_letters+string.digits+string.punctuation
cap=random.choice(s)+random.choice(s)+random.choice(s)+random.choice(s)
print(f"Random string:",cap)