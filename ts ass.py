import numpy as np
import matplotlib.pyplot as plt
time_series = np.array([18.6,19,23,26.3,27,26,24,19.9,16,15,27,28,30,36,38.4,36,34,32,28,26,28.2,32.3,34,22,35.1,37,32,31.8,31.1,
27.4,22,28,29,32,38.4,39.2,39,35.9,33.5,29.6,21,25,26,29,31,33.4,36])
q = int(input("Enter value of q: "))
n = len(time_series)
Tline = np.zeros(n)
if len(time_series) % 2 == 1:
    for i in range(q, n - q):
        Tline[i] = np.mean(time_series[i - q:i + q + 1])
else:
    d = 2 * q
    for i in range(q, n - q):
        Tline[i] = (0.5 * time_series[i - q] + np.sum(time_series[i - q + 1:i + q]) + 0.5 * time_series[i + q]) / d
seasonal_effect = np.zeros(n)
for i in range(n):
    sum_diff = 0
    count = 0
    for j in range(-(n // q), n // q):
        if 0 <= i + j * q < n:
            sum_diff += time_series[i + j * q] - Tline[i + j * q]
            count += 1
    if count > 0:
        seasonal_effect[i] = sum_diff / count
avg_seasonality = np.mean(seasonal_effect)
adjusted_seasonal = seasonal_effect - avg_seasonality
print("Calculated Trend:", Tline)
print("Extracted Seasonality:", adjusted_seasonal)
plt.figure(figsize=(10, 6))
plt.subplot(311)
plt.plot(time_series, label="Original Data")
plt.legend(loc='upper left')
plt.subplot(312)
plt.plot(Tline, label="Trend", color='orange')
plt.legend(loc='upper left')
plt.subplot(313)
plt.plot(adjusted_seasonal, label="Seasonality", color='green')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()