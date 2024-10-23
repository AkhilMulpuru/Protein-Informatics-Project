import matplotlib.pyplot as plt

# Parsed RMSF data (this is an example, use actual values)
residue = list(range(1, 10))  # Update this range based on actual data size.
rmsf_nm = [0.0487, 0.0327, 0.0575, 0.0409, 0.0277, 0.0311, 0.0411, 0.0383, 0.0376]  # Use the full data here.

# Plotting RMSF over residues
plt.figure(figsize=(10, 6))
plt.plot(residue, rmsf_nm, label="RMSF", color='r')
plt.xlabel("Residue")
plt.ylabel("RMS Fluctuation (nm)")
plt.title("RMS Fluctuation per Residue")
plt.grid(True)
plt.legend()

# Save the figure as an image file
plt.savefig('rmsf_plot.png')
