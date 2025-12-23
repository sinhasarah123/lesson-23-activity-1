class Reverse:
    def __init__(self, strings=""):
        self.strings = strings
    
    def reverse_string(self):
        return self.strings[::-1]

# Example usage
user_input = input("Enter a word: ")
reverse_obj = Reverse(user_input)
print(reverse_obj.reverse_string())