import matplotlib.pyplot as plt
import numpy as np

matrix_sizes = [1088, 2112, 3136, 4160, 5184, 6208, 7232, 8256, 9280, 10304]

# data from node01
magma_gflops_node01_updated = [243.16, 295.20, 544.62, 595.42, 575.64, 590.34, 582.88, 586.35, 567.73, 567.91]
cublas_gflops_node01_updated = [289.94, 736.16, 794.56, 803.07, 811.60, 816.94, 817.86, 822.82, 664.25, 981.17]

# # data from node02
# magma_gflops_node02_updated = [237.84, 377.39, 595.64, 594.80, 602.21, 587.65, 578.88, 580.77, 563.40, 563.27]
# cublas_gflops_node02_updated = [269.43, 734.38, 794.83, 803.31, 806.80, 817.01, 812.55, 813.21, 659.59, 972.12]
magma_gflops_desktop = [4148.93, 10724.16, 11755.40, 11744.13, 11993.30, 11970.38, 11915.54, 12130.93, 12103.83, 12034.74]
cublas_gflops_desktop = [1088.76, 19527.13, 14699.60, 24794.99, 26171.84, 26696.50, 27780.62, 30017.74, 29233.23, 30046.24]


# Plotting updated node01 and node02 data for comparison
plt.figure(figsize=(12, 8))

# Node01 updated data
plt.plot(matrix_sizes, magma_gflops_node01_updated, marker='o', linestyle='-', label='Node01: MAGMA Gflop/s')
plt.plot(matrix_sizes, cublas_gflops_node01_updated, marker='s', linestyle='-', label='Node01: cuBLAS Gflop/s')

# # Node02 updated data
# plt.plot(matrix_sizes, magma_gflops_node02_updated, marker='x', linestyle='-', label='Node02: MAGMA Gflop/s')
# plt.plot(matrix_sizes, cublas_gflops_node02_updated, marker='d', linestyle='-', label='Node02: cuBLAS Gflop/s')

# Node02 updated data
plt.plot(matrix_sizes, magma_gflops_desktop, marker='x', linestyle='-', label='4070Ti: MAGMA Gflop/s')
plt.plot(matrix_sizes, cublas_gflops_desktop, marker='d', linestyle='-', label='4070Ti: cuBLAS Gflop/s')


# Labels and title
plt.xlabel('Matrix Size (MxNxK)')
plt.ylabel('Performance (Gflop/s)')
# plt.title('Performance Comparison between MAGMA and cuBLAS on Node01 and Node02')
plt.title('Performance Comparison between MAGMA and cuBLAS on Node01 and Desktop with 4070Ti GPU')
plt.legend()
plt.grid(True)

plt.show()
