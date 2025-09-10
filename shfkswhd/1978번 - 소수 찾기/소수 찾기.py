#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1978                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shfkswhd <boj.kr/u/shfkswhd>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1978                           #+#        #+#      #+#     #
#    Solved: 2025/09/10 22:57:49 by shfkswhd      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
numbers = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = sum(1 for number in numbers if is_prime(number))
print(prime_count)