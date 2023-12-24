numbers = [1, -1, 6, -8, -10, 5, 14, ]


def is_positive(num):
    return num > 0

pos_numbers = filter(is_positive, numbers)
print(pos_numbers)
pos_numbers_list = list(pos_numbers)
print(pos_numbers_list)

#Length<6
words=["Apple", "iPhone", "iPad","Strawberry", "Book", "Mango"]
min_length =6

def is_check_length(words):
    return len(words) < min-length

op = check_len(words[0])
print(op)
op= list(filter(check_len_words))
print(op)



