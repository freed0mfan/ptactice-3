X_Y_N = input('X_Y_N: ')
X = int(X_Y_N.split()[0])
Y = int(X_Y_N.split()[1])
N = int(X_Y_N.split()[2])
price = X * 100 + Y
revenue = price * N
R = revenue // 100
K = revenue % 100
print(f'{R} руб. {K} коп.')

