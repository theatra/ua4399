# Task 1

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(f"In the given text, the word 'better' is used {zen.count("better")} times.")
print(f"In the given text, the word 'never' is used {zen.count("never")} times.")
print(f"In the given text, the word 'is' is used {zen.count("is")} times.")
print(" ")
print(zen.upper())
print(" ")
print(zen.replace("i", "&"))
print(" ")


# Task 2
number = str(1864)
product = 1
sorted_asc = []

for char in number:
    sorted_asc.append(char)
    product *= int(char)

print(product)
print(sorted(sorted_asc))
print(int((number)[::-1]))
print(" ")


# Task 3
a, b = 4, 5
print(f" a = {a}, b = {b}")
b, a = 4, 5
print(f" a = {a}, b = {b}")