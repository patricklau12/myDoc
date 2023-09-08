import matplotlib.pyplot as plt

# Data from the provided table
bytes_ = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
          32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]
time_usec = [76.35, 77.85, 80.12, 75.82, 79.85, 73.05, 62.06, 64.06, 83.58, 101.22,
             134.92, 143.98, 128.88, 158.40, 217.01, 311.00, 441.23, 769.12, 1427.07,
             2638.25, 5076.10, 9994.47, 19691.95, 39536.29]
mbytes_per_sec = [0.00, 0.01, 0.02, 0.05, 0.10, 0.22, 0.52, 1.00, 1.53, 2.53, 3.79,
                  7.11, 15.89, 25.86, 37.75, 52.68, 74.26, 85.21, 91.85, 99.36, 103.29,
                  104.92, 106.50, 106.09]

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot latency on left y-axis
color = 'tab:red'
ax1.set_xlabel('#bytes')
ax1.set_ylabel('t[usec]', color=color)
line1, = ax1.plot(bytes_, time_usec, 'o-', color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Instantiate a second y-axis to plot throughput
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Mbytes/sec', color=color)
line2, = ax2.plot(bytes_, mbytes_per_sec, 's-', color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Set log scale for x-axis to better visualize the data
ax1.set_xscale('log')
ax1.set_title('MPI PingPong Test: Latency and Throughput')

# Create a combined legend in the upper left without overlap
ax1.legend([line1, line2], ["Latency (t[usec])", "Throughput (Mbytes/sec)"], loc="upper left")

# Display the plot with grid lines
plt.grid(True, which="both", ls="--")
plt.show()