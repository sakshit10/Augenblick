def hash_algorithm(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value = (current_value * 17) % 256
    return current_value

def process_initialization_sequence(sequence):
    steps = sequence.split(',')
    total_sum = 0
    for step in steps:
        key, value = step.split('=')
        total_sum += hash_algorithm(value)
    return total_sum


sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
result_sum = process_initialization_sequence(sequence)
print(result_sum)
