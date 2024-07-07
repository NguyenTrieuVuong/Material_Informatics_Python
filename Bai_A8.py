import numpy as np
import matplotlib.pyplot as plt

# Hàm phân bố ρ(x)
def target_distribution(x):
    return (x * (1 - x) * np.exp(x)) / (3 - np.exp(1))

# Hàm phân bố q(x) - một hàm đề xuất dễ vẽ hình và có thể chấp nhận được
def proposal_distribution(x):
    return 1  # Đơn giản lấy hằng số 1 để làm hàm đề xuất

# Phương pháp Rejection
def rejection_sampling(N):
    samples = []
    while len(samples) < N:
        x = np.random.uniform(0, 1)  # Sinh số ngẫu nhiên x từ [0, 1]
        u = np.random.uniform(0, proposal_distribution(x))

        if u <= target_distribution(x):
            samples.append(x)

    return np.array(samples)

# Kiểm tra phân bố xác suất
def plot_probability_distribution(samples):
    plt.hist(samples, bins=50, density=True, label='Sampled Distribution')
    x_values = np.linspace(0, 1, 1000)
    plt.plot(x_values, target_distribution(x_values), label='Target Distribution', color='red', linewidth=2)
    plt.title('Rejection Sampling - Probability Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.show()

# Số lượng mẫu cần sinh
N = 1000

# Sinh mẫu bằng phương pháp Rejection
samples = rejection_sampling(N)

# Kiểm tra phân bố xác suất
plot_probability_distribution(samples)
