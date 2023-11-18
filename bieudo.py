import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu giả định cho nhiệt độ và lượng mưa (thay thế bằng dữ liệu thực nếu có)
months = np.arange(1, 13)
mean_temperature = [25.5 , 26.1, 27.3, 28.6, 28.4, 27.7, 27.3, 27.1, 27, 26.8, 26.7, 25.8]
rainfall = [8.1, 1.8, 6.6, 41.3, 149.7, 203.2, 189.2, 192.6, 231.3, 263.7, 95.4, 35.6]

# Tạo figure và trục cho biểu đồ lượng mưa (trục bên trái)
fig, ax1 = plt.subplots(figsize=(8, 5))

# Vẽ biểu đồ lượng mưa trên trục ax1
ax1.bar(months, rainfall, color='blue', alpha=0.5)
ax1.set_ylabel('Lượng mưa (mm)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Tạo trục cho biểu đồ nhiệt độ (trục bên phải)
ax2 = ax1.twinx()

# Vẽ biểu đồ nhiệt độ trên trục ax2
ax2.plot(months, mean_temperature, marker='o', color='red')
ax2.set_ylabel('Nhiệt độ (°C)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Thiết lập các thông số trục x
ax1.set_xlabel('Tháng')
ax1.set_xticks(months)
ax1.set_xticklabels(['{}'.format(m) for m in months])

# Tiêu đề của biểu đồ
plt.title('Biểu đồ Lượng mưa và Nhiệt độ theo tháng')

# Hiển thị biểu đồ
plt.grid(True)
plt.show() 
