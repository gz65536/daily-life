from matplotlib import pyplot as plt
import math

# A numerical proof of: The density of basic Pythagorean numbers converge to 1/2pi. 

N = 10000
series = []
avg_series = []
for i in range(N):
	tmp_series = []
	for j in range(i):
		if j is not 0:
			tmp = (i ** 2 - j ** 2) ** 0.5
			# print("i = %d, j = %d, tmp = %f" % (i, j, tmp))
			if tmp > j and tmp.is_integer() and math.gcd(i, math.gcd(j, int(tmp))) == 1:
				tmp_series.append(j)
	if len(tmp_series) is not 0:
		series.append(len(tmp_series))
	else:
		series.append(0)
	avg_series.append(sum(series) / len(series))

plt.plot(avg_series)
plt.hlines(y = 0.5 / math.pi, xmin = 0, xmax = N, color = 'r')
plt.show()