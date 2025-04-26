def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

def main():
    while True:
        try:
            number = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You must enter a valid integer.")

    while number != 1:
        number = collatz(number)

if __name__ == "__main__":
    main()
