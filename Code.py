class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5 == 0:
                l.append('FizzBuzz')
            else:
                if x%3 == 0 or x%5 == 0:
                    if x%3 == 0:
                        l.append('Fizz')
                    if x%5 == 0:
                        l.append('Buzz')
                else:
                    l.append(str(x))
        return l
