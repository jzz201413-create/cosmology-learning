from scipy.optimize import root_scalar
from scipy.special import ellipk
import math
import matplotlib.pyplot as plt


# =========================
# Basic settings
# =========================

Z_max = 10
W_max = 3
M = 1


# =========================
# Create two figures
# =========================

fig_all = plt.figure()
fig_zoom = plt.figure()


# =========================
# Colors for different w
# =========================

colors = plt.cm.viridis(
    [w / W_max for w in range(W_max + 1)]
)


# =========================
# Enumerate z, v, w
# =========================

for z in range(1, Z_max + 1):

    if z == 1:
        v_values = [0]
    else:
        v_values = range(1, z)

    for v in v_values:

        if math.gcd(z, v) != 1:
            continue

        for w in range(W_max + 1):

            q = w + v / z

            if q == 0:
                continue

            # =========================
            # Calculate one branch
            # =========================

            LE_data = []

            for i in range(1, 100):

                e = i / 100

                def f(lambda_):

                    m = (
                        4 * M * e
                        /
                        (
                            lambda_
                            + 2 * M * (e - 3)
                        )
                    )

                    K = ellipk(m)

                    return (
                        math.pi / 2
                        * (q + 1)
                        * math.sqrt(
                            1
                            + 2 * M / lambda_
                            * (e - 3)
                        )
                        - K
                    )

                result = root_scalar(
                    f,
                    bracket=(
                        6 + 2 * e + 1e-8,
                        100
                    )
                )

                lambda_ = result.root

                # =========================
                # Energy E
                # =========================

                E = (
                    (
                        lambda_**2
                        - 4 * M * lambda_
                        + 4 * M**2
                        - 4 * M**2 * e**2
                    )
                    /
                    (
                        lambda_
                        * (
                            lambda_
                            - 3 * M
                            - M * e**2
                        )
                    )
                ) ** 0.5

                # =========================
                # Angular momentum L
                # =========================

                L = (
                    lambda_
                    * (
                        M
                        /
                        (
                            lambda_
                            - 3 * M
                            - M * e**2
                        )
                    ) ** 0.5
                )

                LE_data.append((L, E))

            # =========================
            # Extract L and E
            # =========================

            L_data = [
                point[0]
                for point in LE_data
            ]

            E_data = [
                point[1]
                for point in LE_data
            ]

            # =========================
            # Overall figure
            # =========================

            plt.figure(fig_all.number)

            plt.plot(
                L_data,
                E_data,
                color=colors[w]
            )

            # =========================
            # Zoomed figure
            # =========================

            plt.figure(fig_zoom.number)

            plt.plot(
                L_data,
                E_data,
                color=colors[w]
            )


# =========================
# Overall figure settings
# =========================

plt.figure(fig_all.number)

plt.xlabel("L")
plt.ylabel("E")

plt.title(
    "Periodic Schwarzschild Orbits"
)

plt.xlim(3.4, 6.5)
plt.ylim(0.94, 1.0)


# Legend
for w in range(W_max + 1):

    plt.plot(
        [],
        [],
        color=colors[w],
        label=f"w = {w}"
    )

plt.legend()


# =========================
# Zoomed figure settings
# =========================

plt.figure(fig_zoom.number)

plt.xlabel("L")
plt.ylabel("E")

plt.title(
    "Periodic Schwarzschild Orbits: Dense Region"
)

plt.xlim(3.5, 3.6)
plt.ylim(0.94, 0.96)


# Legend
for w in range(W_max + 1):

    plt.plot(
        [],
        [],
        color=colors[w],
        label=f"w = {w}"
    )

plt.legend()


# =========================
# Show figures
# =========================

plt.show()
