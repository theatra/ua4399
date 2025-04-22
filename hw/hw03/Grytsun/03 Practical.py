text = """
Sparse is better than dense.
Readability counts.
If the implementation is easy to explain, it may be a good idea.
"""
# Вивід тексту
print(f"Count 'better' == {text.count("better")}")
print(f"Count 'never == {text.count("never")}")
print(f"Count 'is' == {text.count("is")}")

# Вивід uppercase
text_upper = text.upper()
print("\nUppercase:\n", text_upper)

# Заміна "i" на "&"
text_replaced = text.replace("i", "&")
print("\nWith replaced 'i':\n", text_replaced)