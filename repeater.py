# count = int(input("How many times do I have to tell you? "))

# print("clean up your room \n" * count)

for i in range(1,21):
    if i == 4 or i == 13:
        print(f"{i} is unlucky")
    elif i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")