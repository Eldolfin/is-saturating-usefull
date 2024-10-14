from matplotlib import pyplot as plt

N_MINUTES = 250
N_FACTORIES = 8
ITEM_STACK = 200
INPUT = 20  # total items / min
USAGE = INPUT / N_FACTORIES  # items / min / factory
OUTPUT = 1  # items / min / factory

time = range(N_MINUTES)

saturating = []
not_saturating = []

# number of items in factories array
factories_saturating = [0] * N_FACTORIES
factories_not_saturating = [0] * N_FACTORIES

saturated = False

for t in time:
    saturating.append(0)
    not_saturating.append(0)

    # saturating
    input_left = INPUT
    for i, items in enumerate(factories_saturating):
        if items < ITEM_STACK:
            adding = min(ITEM_STACK - items, input_left)
            input_left -= adding
            factories_saturating[i] += adding
    saturated = saturated or input_left > 0

    if saturated:
        for i, items in enumerate(factories_saturating):
            if items >= USAGE:
                factories_saturating[i] -= USAGE
                saturating[-1] += OUTPUT

    # not saturating
    input_left = INPUT
    for i, items in enumerate(factories_not_saturating):
        if items <= ITEM_STACK - INPUT:
            adding = min(ITEM_STACK - items, input_left)
            input_left -= adding
            factories_not_saturating[i] += adding
            break

    for i, items in enumerate(factories_not_saturating):
        if items >= USAGE:
            factories_not_saturating[i] -= USAGE
            not_saturating[-1] += OUTPUT


produced_saturating = [saturating[0]]
produced_not_saturating = [not_saturating[0]]

for t in range(1, N_MINUTES):
    produced_saturating.append(produced_saturating[-1] + saturating[t])
    produced_not_saturating.append(produced_not_saturating[-1] + not_saturating[t])

plt.figure(figsize=(10, 10))

plt.subplot(211)
plt.title("Instant production")
plt.plot(time, saturating, label="saturating")
plt.plot(time, not_saturating, label="not saturating")
plt.xlabel("Minutes passed")
plt.ylabel("Item produced/min")
plt.legend()

plt.subplot(212)
plt.title("Total produced")
plt.plot(time, produced_saturating, label="saturating")
plt.plot(time, produced_not_saturating, label="not saturating")
plt.xlabel("Minutes passed")
plt.ylabel("Item produced")
plt.legend()

plt.savefig("figure.png")
plt.show()
