n = int(input())
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for coin in coin_types:
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    count += n // coin
    n %= coin

print(count)
