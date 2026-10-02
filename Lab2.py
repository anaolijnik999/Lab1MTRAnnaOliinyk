import math

firm1 = [(0.90, 5), (0.10, -10)]
firm2 = [(0.95, 10), (0.05, -25)]

def stats(data):
    mean = sum(p * x for p, x in data)
    var = sum(p * (x - mean) ** 2 for p, x in data)
    std = math.sqrt(var)
    cv = std / mean
    ssv = math.sqrt(sum(p * (x - mean) ** 2 for p, x in data if x < mean))
    csv = ssv / mean
    loss_prob = sum(p for p, x in data if x <= 0)
    expected_loss = sum(p * x for p, x in data if x <= 0)
    return {
        "mean": mean, "var": var, "std": std, "cv": cv,
        "ssv": ssv, "csv": csv, "loss_prob": loss_prob,
        "expected_loss": expected_loss,
    }

results = {}
for name, data in [("Firm 1", firm1), ("Firm 2", firm2)]:
    r = stats(data)
    results[name] = r
    print(f"\n{name}")
    for key, value in r.items():
        print(f"  {key} = {round(value, 3)}")

print("\nConclusion")
print("highest expected profit:", max(results, key=lambda n: results[n]["mean"]))
print("lowest absolute risk (std):", min(results, key=lambda n: results[n]["std"]))
print("lowest relative risk (cv):", min(results, key=lambda n: results[n]["cv"]))
print("lowest downside risk (ssv):", min(results, key=lambda n: results[n]["ssv"]))
print("lowest relative downside risk (csv):", min(results, key=lambda n: results[n]["csv"]))
print("lowest loss probability:", min(results, key=lambda n: results[n]["loss_prob"]))
print("smallest expected loss:", max(results, key=lambda n: results[n]["expected_loss"]))