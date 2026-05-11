import pandas as pd
import matplotlib.pyplot as plt

# Load the security log dataset
df = pd.read_csv("data/security_logs.csv")

# Show first few rows
print("\n=== Security Logs ===")
print(df.head())

# Filter failed logins
failed_logins = df[df["status"] == "FAILED"]

print("\n=== Failed Login Attempts ===")
print(failed_logins)

# Count failed login attempts by IP address
failed_ip_counts = failed_logins["ip_address"].value_counts()

print("\n=== Failed Login Count by IP ===")
print(failed_ip_counts)

# Detect suspicious IPs (3 or more failed attempts)
suspicious_ips = failed_ip_counts[failed_ip_counts >= 3]

print("\n=== Suspicious IP Addresses ===")
print(suspicious_ips)

# Create visualization
failed_ip_counts.plot(kind="bar")

plt.title("Failed Login Attempts by IP")
plt.xlabel("IP Address")
plt.ylabel("Number of Failed Attempts")

plt.tight_layout()

# Save chart image
plt.savefig("images/failed_login_chart.png")

# Show chart
plt.show()
