#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30802                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: shfkswhd <boj.kr/u/shfkswhd>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30802                          #+#        #+#      #+#     #
#    Solved: 2025/09/09 23:26:06 by shfkswhd      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# T * n (S, M, L, XL, XXL, XXXL)
# P * n + 1 * m (m < P)
# N명 중
# sum(S,M,L,XL,XXL,XXXL) = N
# 펜은 N//P 하고 N%P 개수만큼 1개씩 더 줌
# 옷은 S,M,L,XL,XXL,XXXL 중 각 T로 나눈 몫에 나머지 있으면 묶음+1
N = int(input())
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

shirt_bundles = 0
shirt_bundles += (S + T - 1) // T
shirt_bundles += (M + T - 1) // T  
shirt_bundles += (L + T - 1) // T
shirt_bundles += (XL + T - 1) // T
shirt_bundles += (XXL + T - 1) // T
shirt_bundles += (XXXL + T - 1) // T

pen_bundles = N // P
pen_extra = N % P

print(f"{shirt_bundles}\n{pen_bundles} {pen_extra}")