from textnode import TextNode

def main():
    dummy = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(dummy)

s = "Test hi new words hi"

print(s.split("hi", 2))

main()