
# Input the String
original_text = "Sip coffee, write code, repeat."

# Display Function
def display(Original, reversed):
  print(f"Original: {Original}")
  print(f"Reversed: {reversed}")

# Function Call
display(original_text, reversed_text)


# 1.Reverses a string using slicing
def reverse_string_slice(text):
  return text[::-1]

reversed_text = reverse_string_slice(original_text)


# 2.For loop
def reverse_string_forloop(text):
  reversed_text = ""
  for char in text:
    reversed_text = char + reversed_text
  return reversed_text

reversed_text = reverse_string_forloop(original_text)


# 3.built-in method reversed()
def reverse_string_reversed(text):
  return ''.join(reversed(text))

reversed_text = reverse_string_reversed(original_text)


# 4.map() function
def reverse_string_map(text):
  return ''.join(map(lambda x: x[::-1], text))

reversed_text = reverse_string_map(original_text)


# 5.List comprehension with join()
def reverse_string_listcomp(text):
  return ''.join([i[::-1] for i in text])

reversed_text = reverse_string_listcomp(original_text)

# 6.While loop with join()
def reverse_string_whileloop(text):
    reversed_string = ''
    i = len(text) - 1
    while i >= 0:
        reversed_string += text[i]
        i -= 1
    return ''.join([i[::-1] for i in text])

reversed_text = reverse_string_whileloop(original_text)


# 7.Recursion
def reverse_string_recursion(text):
    if len(text) == 1:
        return text
    return reverse_string_recursion(text[1:]) + text[0]

reversed_text = reverse_string_recursion(original_text)

# 8.itertools
import itertools

def reverse_string_itertools(text):
    return ''.join(itertools.chain(reversed(text)))

reversed_text = reverse_string_itertools(original_text)