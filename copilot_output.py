def find_nth_prime(n):
    """Find the nth prime number."""
    if n < 1:
        return None
    
    primes = []
    candidate = 2
    
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(candidate)
        
        candidate += 1
    
    return primes[n - 1]

def find_first_palindrome_after_100():
    """Find the first palindrome number after 100."""
    num = 101
    while True:
        # Convert number to string and check if it reads the same forwards and backwards
        if str(num) == str(num)[::-1]:
            return num
        num += 1

def main():
    result = find_first_palindrome_after_100()
    print(result)

if __name__ == "__main__":
    main()