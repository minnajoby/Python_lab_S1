def even_perfect_squares(start, end):
    results = []
    for num in range(start, end + 1):
        if 1000 <= num <= 9999 and num % 2 == 0:
            root = int(num**0.5)
            if root * root == num: 
                digits = str(num)
                if all(int(digit) % 2 == 0 for digit in digits):
                    results.append(num)
    return results
start_range = int(input("Enter start range: "))
end_range = int(input("Enter end range: "))
print(f"Four-digit even perfect squares: {even_perfect_squares(start_range, end_range)}")
