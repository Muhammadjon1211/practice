import turtle
print('=== Python Packages & Core Package ===')
'''Pyhthon packages: core, file, external'''
# Core packages

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(250)

# turtle.done()
my_file = open('material/message.txt')
try:
    content = my_file.read()
    print("context:", content)
finally:
    my_file.close()

# with - Context manager
with open('material/message.txt') as your_file:
    your_content = your_file.read()
    print("your content:", your_content)
