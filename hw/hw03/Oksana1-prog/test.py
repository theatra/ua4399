import sys, cStringIO
zen = cStringIO.StringIO()
old_stdout = sys.stdout
sys.stdout = zen
sys.stdout = old_stdout
print zen.getvalue()
The Zen of Python, by Tim Peters