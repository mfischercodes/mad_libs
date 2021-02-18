user_type_list = ['color', 'flower', 'dog breed']

user_input_list = []
for type_words in user_type_list:
    user_input = input('Enter a {}: '.format(type_words))
    user_input_list.append(user_input)

print("""
Roses are {}
{} are blue
my type of dog is a {}
""".format(user_input_list[0],user_input_list[1],user_input_list[2]))



