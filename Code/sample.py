import random
import sys
from frequency import histogram

def generate_random_word(source_text):

    histogram_sample = histogram(source_text)

    random_word = histogram_sample[random.randint(0,len(histogram_sample)-1)][0]

    return random_word












if __name__ == "__main__":
    file = sys.argv[1]

    random_word = generate_random_word(file)
    print(random_word)
