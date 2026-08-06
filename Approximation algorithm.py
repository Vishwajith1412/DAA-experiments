def first_fit(items, capacity=1.0):
    bins = []  # Each bin stores remaining space
    bin_contents = []
    for item in items:
        placed = False
        for i, space in enumerate(bins):
            if round(space, 4) >= round(item, 4):
                bins[i] = round(bins[i] - item, 4)
                bin_contents[i].append(item)
                placed = True
                break
        if not placed:
            bins.append(round(capacity - item, 4))
            bin_contents.append([item])
    return bin_contents

def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)

def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    bins = []
    bin_contents = []
    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')
        for i, space in enumerate(bins):
            if round(space, 4) >= round(item, 4) and round(space - item, 4) < best_space:
                best_space = round(space - item, 4)
                best_idx = i
        if best_idx >= 0:
            bins[best_idx] = round(bins[best_idx] - item, 4)
            bin_contents[best_idx].append(item)
        else:
            bins.append(round(capacity - item, 4))
            bin_contents.append([item])
    return bin_contents

def display_bins(label, bins):
    print(f'\n{label}: {len(bins)} bins')
    for i, b in enumerate(bins, 1):
        used = sum(b)
        bar = '#' * int(round(used, 2) * 20)
        print(f' Bin {i}: {[round(x,1) for x in b]} | Used: {used:.1f} [{bar:<20}]')

# --- Updated Inputs ---
items = [0.6, 0.8, 0.2, 0.9, 0.4, 0.3, 0.7, 0.5, 0.1, 0.5]
capacity = 1.0

lower_bound = -(-sum(items) // capacity)  # Ceiling division
print(f'Items: {items}')
print(f'Capacity: {capacity}')
print(f'Sum of items: {sum(items):.1f}')
print(f'Lower bound on bins: {int(lower_bound)}')

ff_bins = first_fit(items)
ffd_bins = first_fit_decreasing(items)
bfd_bins = best_fit_decreasing(items)

display_bins('First Fit (FF)', ff_bins)
display_bins('First Fit Decreasing (FFD)', ffd_bins)
display_bins('Best Fit Decreasing (BFD)', bfd_bins)

print(f'\nSummary: Lower Bound={int(lower_bound)}, FF={len(ff_bins)}, FFD={len(ffd_bins)}, BFD={len(bfd_bins)}')
