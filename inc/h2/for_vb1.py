import numpy as np

data = np.array([1,2,3,4,5,6]) # een test array

# De volgende for-loop print een voor een alle getallen in data
# i is hierbij het getal dat loopt van 0 tot len(data) = 6
for i in range(len(data)):
    print(data[i])