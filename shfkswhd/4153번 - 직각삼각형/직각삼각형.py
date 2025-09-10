#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4153                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: MakeDr <boj.kr/u/MakeDr>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4153                           #+#        #+#      #+#     #
#    Solved: 2025/09/09 22:43:04 by MakeDr        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

while True:
    a,b,c = sorted(map(int, input().split()))
    if a == 0 and b == 0 and c == 0:
        break
    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")