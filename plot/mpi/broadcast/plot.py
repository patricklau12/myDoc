import matplotlib.pyplot as plt

# Data
message_sizes = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192,
                16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]
average_times_2 = [0.11, 36.66, 35.38, 34.30, 62.09, 36.53, 35.01, 60.19, 34.91, 131.84, 131.97,
                   165.83, 207.13, 260.46, 291.83, 321.38, 503.01, 832.86, 1434.41, 2790.49, 4879.73, 9509.85, 19289.88, 38982.78]
average_times_4 = [0.20, 319.12, 908.68, 303.86, 460.32, 214.77, 849.20, 268.76, 216.32, 260.63, 333.10,
                   373.08, 369.69, 388.72, 475.32, 676.12, 986.46, 1587.48, 2871.02, 5316.53, 10000.10, 19509.67, 38512.89, 78827.89]
average_times_8 = [0.17, 326.57, 362.88, 465.85, 270.96, 434.08, 295.43, 324.27, 250.05, 288.01, 341.74,
                   374.85, 370.21, 388.37, 471.45, 722.92, 1007.21, 1752.47, 2955.48, 5381.08, 10602.26, 36094.40, 62971.28, 269391.44]
average_times_16 = [0.13, 332.26, 242.41, 351.44, 268.50, 435.28, 207.03, 324.95, 401.95, 267.80, 354.97,
                    397.05, 404.45, 439.52, 486.84, 722.92, 1114.19, 1750.26, 2955.48, 5381.08, 13388.32, 92184.85, 195937.18, 269391.44]
average_times_24 = [0.12, 216.56, 259.16, 570.00, 556.83, 435.28, 239.06, 324.95, 309.18, 267.80, 354.97,
                    397.05, 400.08, 427.03, 488.28, 9601.28, 11782.98, 13413.68, 17039.14, 25174.43, 41380.81, 106518.39, 188176.10, 347368.19]

# Filtering the data to start from 256 bytes
start_index = message_sizes.index(256)
filtered_message_sizes = message_sizes[start_index:]
filtered_avg_times_2 = average_times_2[start_index:]
filtered_avg_times_4 = average_times_4[start_index:]
filtered_avg_times_8 = average_times_8[start_index:]
filtered_avg_times_16 = average_times_16[start_index:]
filtered_avg_times_24 = average_times_24[start_index:]

colors = ['b', 'g', 'r', 'c', 'm']

# Plotting the filtered data
plt.figure(figsize=(12, 7))
plt.plot(filtered_message_sizes, filtered_avg_times_2, '-o', color=colors[0], label="2 cores")
plt.plot(filtered_message_sizes, filtered_avg_times_4, '-o', color=colors[1], label="4 cores")
plt.plot(filtered_message_sizes, filtered_avg_times_8, '-o', color=colors[2], label="8 cores")
plt.plot(filtered_message_sizes, filtered_avg_times_16, '-o', color=colors[3], label="16 cores")
plt.plot(filtered_message_sizes, filtered_avg_times_24, '-o', color=colors[4], label="24 cores")

# Adjusting the plot
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Average Time (usec)')
plt.title('Bcast Performance for Different Number of Processes (Starting from 256 bytes)')
plt.legend()
plt.grid(True, which="both", ls="--")

# Display the plot
plt.tight_layout()
plt.show()

# Save the plot to a file
file_path = "./plot.png"
plt.savefig(file_path)

