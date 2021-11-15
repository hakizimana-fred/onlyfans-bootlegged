import random  
import string  

def file_random(length):  
    sample_string = 'pqrstuvwxy'
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    return result