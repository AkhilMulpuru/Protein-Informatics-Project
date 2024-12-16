import matplotlib.pyplot as plt

# Parsed RMSD data
time_ns = [
    0.0000000, 0.0020000, 0.0040000, 0.0060000, 0.0080000, 0.0100000, 0.0120000, 0.0140000,
    0.0160000, 0.0180000, 0.0200000, 0.0220000, 0.0240000, 0.0260000, 0.0280000, 0.0300000,
    # Add the remaining time points
]

rmsd_nm = [
    0.0000000, 0.0473701, 0.0463034, 0.0549544, 0.0534957, 0.0504536, 0.0549290, 0.0537580,
    0.0579195, 0.0535025, 0.0534018, 0.0562000, 0.0538608, 0.0535592, 0.0576662, 0.0559172,
    # Add the remaining RMSD values
]

# Plotting RMSD over time
plt.figure(figsize=(10, 6))
plt.plot(time_ns, rmsd_nm, label="RMSD", color='b')
plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("RMSD over Time (ns)")
plt.grid(True)
plt.legend()

# Save the figure as an image
plt.savefig("rmsd_plot.png")

