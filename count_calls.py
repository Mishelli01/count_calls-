calls = 0
def count_calls():
  global calls
  calls+=1

def string_info (same_str):
    count_calls()
    return len(same_str), same_str.upper(), same_str.lower()
def is_contains(same_str, same_list):
    count_calls()
    for i in same_list:
        if same_str in same_list:
             return True
        else:
            return False
print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)