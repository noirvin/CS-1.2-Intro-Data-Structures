import random
import sys
from frequency import histogram

def total_weight(histogram):

    weight = 0
    for element in histogram:
        weight += element[1]
    return weight


def generate_random_word(source_text):

    histogram_sample = histogram(source_text)

    weight_sum = 0
    count = 0

    while count < len(histogram_sample):

        weight_sum += ((histogram_sample[count][1])/total_weight(histogram_sample))*100
        count+=1

    random_num = random.randint(0,int(weight_sum))

    for element in histogram_sample:

        random_num = weight_sum - random_num

        if random_num <= 0:
            print("Hello")
            generated_word = element[0]
            return generated_word
            break

        else:


            continue
















if __name__ == "__main__":
    file = sys.argv[1]

    random_word = generate_random_word(file)
    print(random_word)
