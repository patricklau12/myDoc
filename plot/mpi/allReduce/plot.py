import matplotlib.pyplot as plt

# Data for 2 processes
t_avg_2 = [0.50, 79.41, 73.86, 165.40, 169.09, 175.60, 169.83, 186.80, 318.72, 355.62, 
           580.20, 540.88, 577.59, 681.77, 848.31, 1274.95, 2128.30, 3743.13, 6628.15, 
           12306.32, 24005.27, 53562.66]

# Data for 4 processes
t_avg_4 = [1.12, 229.39, 230.38, 452.24, 454.58, 444.72, 454.01, 463.18, 690.21, 956.10, 
           1175.17, 1373.82, 1261.20, 1482.18, 1835.84, 2466.80, 3749.87, 7309.19, 11968.28, 
           43281.51, 51849.59, 102066.71]

# Data for 8 processes
t_avg_8 = [0.86, 242.29, 248.02, 478.92, 481.18, 460.36, 470.52, 466.96, 713.56, 962.63, 
           1185.89, 1370.75, 1252.93, 1442.43, 1824.42, 2534.52, 3649.41, 6359.58, 10338.33, 
           29072.68, 73410.19, 122067.49]

# Data for 16 processes
t_avg_16 = [0.60, 240.23, 237.13, 478.92, 481.18, 494.99, 473.99, 490.91, 713.56, 962.63, 
            1175.75, 1336.08, 1252.93, 1442.43, 1883.87, 2690.24, 3897.30, 6359.58, 10817.75, 
            20759.50, 55562.51, 111791.48]


# Data extraction for 24 processes
t_avg_24 = [0.54, 310.04, 258.10, 501.10, 512.81, 525.32, 492.82, 524.78, 751.72, 1000.40, 
            1333.19, 1410.83, 1427.04, 1730.96, 1914.52, 2534.52, 3771.23, 6125.61, 12419.53, 
            27904.06, 55847.31, 109895.94]

# Data organization
data = {
    "bytes": [0, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304],
    "2": t_avg_2,
    "4": t_avg_4,
    "8": t_avg_8,
    "16": t_avg_16,
    "24": t_avg_24
}

# List of processes (core counts)
processes = [2, 4, 8, 16, 24]

# Extracting the relevant data range (from 4KB to 4MB)
start_idx = data["bytes"].index(4096)  # 4KB
end_idx = data["bytes"].index(4194304) + 1  # 4MB

# Relevant message sizes
message_sizes = data["bytes"][start_idx:end_idx]

# Using a distinguishable color palette
colors = ['b', 'g', 'r', 'c', 'm', 'y']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

for i, core_count in enumerate(processes):
    latencies = data[str(core_count)][start_idx:end_idx]
    ax.plot(message_sizes, latencies, marker='o', linestyle='-', label=f"{core_count} cores", color=colors[i])

ax.set_xscale("log", base=2)
ax.set_xticks(message_sizes)
ax.set_xticklabels([f"{size // 1024}KB" if size < 1048576 else f"{size // (1024*1024)}MB" for size in message_sizes])
ax.set_xlabel("Message Size (Bytes)")
ax.set_ylabel("Average Latency (usec)")
ax.set_title("Allreduce Average Latency for Different Core Counts")
ax.legend(loc='upper left')
ax.grid(True, which="both", ls="--", c='0.7')

plt.show()
fig.savefig("./plot.png")