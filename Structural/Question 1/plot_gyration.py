import matplotlib.pyplot as plt

# Parsed Radius of Gyration data
time_ps = [
    0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0,
    32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58.0, 60.0
]

rg_nm = [
    1.90019, 1.89873, 1.90077, 1.89623, 1.89742, 1.89566, 1.89663, 1.89479, 1.89493, 1.89518,
    1.89781, 1.89667, 1.89654, 1.89821, 1.89689, 1.89575, 1.89643, 1.89754, 1.89712, 1.89668,
    1.89699, 1.89711, 1.89743, 1.89787, 1.89813, 1.89843, 1.89785, 1.89798, 1.89812, 1.89823, 1.89787
]

# Ensure time_ps and rg_nm have the same length
if len(time_ps) != len(rg_nm):
    print(f"Error: time_ps and rg_nm have different lengths: {len(time_ps)} and {len(rg_nm)}")
else:
    # Plotting Radius of Gyration over time
    plt.figure(figsize=(10, 6))
    plt.plot(time_ps, rg_nm, label="Radius of Gyration", color='g')
    plt.xlabel("Time (ps)")
    plt.ylabel("Radius of Gyration (nm)")
    plt.title("Radius of Gyration over Time (ps)")
    plt.grid(True)
    plt.legend()

    # Save the figure instead of showing it
    plt.savefig('gyration_plot.png')
    print("Plot saved as 'gyration_plot.png'")
