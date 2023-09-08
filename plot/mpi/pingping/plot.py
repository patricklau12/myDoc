import matplotlib.pyplot as plt

# Redefining the PingPing data
bytes_pingping = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
                  32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]
time_usec_pingping = [128.21, 124.18, 126.48, 146.29, 124.50, 124.01, 123.85, 124.44, 
                      124.70, 143.54, 174.73, 280.57, 280.05, 279.83, 349.75, 450.38, 
                      637.51, 1005.48, 1673.25, 2999.85, 5834.03, 11234.28, 22473.95, 50070.02]
mbytes_per_sec_pingping = [0.00, 0.01, 0.02, 0.03, 0.06, 0.13, 0.26, 0.51, 1.03, 1.78, 
                           2.93, 3.65, 7.31, 14.64, 23.42, 36.38, 51.40, 65.18, 78.33, 
                           87.39, 89.87, 93.34, 93.31, 83.77]

# Re-plotting the data
fig, ax1 = plt.subplots(figsize=(12, 6))

# Extracting the relevant data range (from 4KB to 4MB)
start_idx = bytes_pingping["bytes"].index(0)  # 4KB
end_idx = bytes_pingping["bytes"].index(4194304) + 1  # 4MB

# Plot latency
color = 'tab:orange'
ax1.set_xlabel('#bytes')
ax1.set_ylabel('t[usec]', color=color)
line1, = ax1.plot(bytes_pingping, time_usec_pingping, 'o-', color=color, label="Latency (t[usec])")
ax1.tick_params(axis='y', labelcolor=color)


# Plot throughput on a second y-axis
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Mbytes/sec', color=color)
line2, = ax2.plot(bytes_pingping, mbytes_per_sec_pingping, 's-', color=color, label="Throughput (Mbytes/sec)")
ax2.tick_params(axis='y', labelcolor=color)

# Create a combined legend in the upper left without overlap
ax1.legend([line1, line2], ["Latency (t[usec])", "Throughput (Mbytes/sec)"], loc="upper left")

# Log scale for x-axis
ax1.set_xscale('log')
ax1.set_title('MPI PingPing Test: Latency and Throughput')

# Display the plot
plt.grid(True, which="both", ls="--")
plt.show()

fig.savefig("./latency_throughput.png")
