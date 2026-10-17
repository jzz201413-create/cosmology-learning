
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ============================================================
# Part 1: Weak-field hypocycloid
# Paper Section 4: Eqs. (5), (8), (12), (24)
# ============================================================

def simulate_weak_field(
    B=0.001,
    e=0.5,
    r_star=6.0,
    t_end=30000.0,
    max_step=2.0,
):
    P = 0.0

    Lambda_star = 1 + B**2 * r_star**2 / 4
    E = Lambda_star
    L = e * B * r_star**2 / (2 * Lambda_star)

    def Lambda(r):
        return 1 + B**2 * r**2 / 4

    def Lambda_prime(r):
        return B**2 * r / 2

    def equations(tau, state):
        r, r_dot, phi = state

        lam = Lambda(r)
        lam_prime = Lambda_prime(r)

        U = L - e * B * r**2 / (2 * lam)

        r_ddot = (
            -(lam_prime / lam) * r_dot**2
            + (P**2 - E**2) * lam_prime / lam**5
            + (1 / r**3)
            * (1 - r * lam_prime / lam)
            * U**2
            + (e * B * lam / r)
            * (1 - r * lam_prime / (2 * lam))
            * U
        )

        phi_dot = lam**2 / r**2 * U

        return [r_dot, r_ddot, phi_dot]

    y0 = [r_star, 0.0, 0.0]

    sol = solve_ivp(
        equations,
        (0.0, t_end),
        y0,
        method="DOP853",
        rtol=1e-10,
        atol=1e-12,
        max_step=max_step,
    )

    if not sol.success:
        raise RuntimeError(sol.message)

    r = sol.y[0]
    phi = sol.y[2]

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    print("\nWeak-field parameters")
    print(f"B = {B}")
    print(f"e = {e}")
    print(f"r_star = {r_star}")
    print(f"Lambda_star = {Lambda_star:.10f}")
    print(f"E = {E:.10f}")
    print(f"L = {L:.10f}")

    return x, y


# ============================================================
# Part 2: Perturbed circular orbit
# Paper Section 3: Eqs. (13)-(21)
# ============================================================

def simulate_perturbed_circular_orbit(
    B=0.1,
    e=18.068,
    r0=6.0,
    epsilon=0.01,
    points_per_radial_period=5000,
):
    # Eq. (14): lower-sign branch
    radicand = 4 * e**2 + 8 - 6 * B**2 * r0**2

    if radicand < 0:
        raise ValueError("The square root in Eq. (14) is not real.")

    L = (
        2
        * (
            3 * B**2 * e * r0**2
            - 2 * np.sqrt(radicand)
        )
        * r0**2
        * B
        / (
            (3 * B**2 * r0**2 - 4)
            * (4 + B**2 * r0**2)
        )
    )

    # Eq. (13): energy squared
    E_squared = (
        (4 * L + 2 * e * B * r0**2 - L * B**2 * r0**2)
        * (4 * L - 2 * e * B * r0**2 + L * B**2 * r0**2)
        * (4 + B**2 * r0**2)**3
        / (512 * B**2 * r0**4)
    )

    if E_squared <= 0:
        raise ValueError(
            f"E^2 = {E_squared} is not positive. "
            "Check the parameter branch and equations."
        )

    E = np.sqrt(E_squared)

    # Eq. (17): radial oscillation frequency
    omega_squared = (
        2
        * (
            3 * B**6 * r0**6 * L**2
            - 12 * e * B**5 * r0**6 * L
            + 12 * e**2 * B**4 * r0**6
            - 16 * B**2 * r0**2 * L**2
            + 128 * L**2
        )
        / (r0**4 * (4 + B**2 * r0**2)**3)
    )

    if omega_squared <= 0:
        raise ValueError("omega^2 is not positive.")

    omega = np.sqrt(omega_squared)

    # Eq. (19a): unperturbed angular frequency
    beta0 = (
        (4 * L + L * B**2 * r0**2 - 2 * e * B * r0**2)
        * (4 + B**2 * r0**2)
        / (16 * r0**2)
    )

    # Eq. (19b)
    beta1 = (
        16 * L - L * B**6 * r0**4 + 2 * e * B**3 * r0**4
    ) / (8 * r0**3)

    # Eq. (21)
    zeta = beta1 * epsilon / beta0

    # Integrate over approximately one full angular revolution:
    # |beta0| * tau_end = 2*pi
    tau_end = 2 * np.pi / abs(beta0)

    # Number of radial periods covered in this time
    radial_period = 2 * np.pi / omega
    num_radial_periods = int(np.ceil(tau_end / radial_period))

    num_points = max(
        1000,
        num_radial_periods * points_per_radial_period,
    )

    tau = np.linspace(0.0, tau_end, num_points)

    # Eqs. (20a), (20b): first-order perturbation
    r = r0 + epsilon * np.cos(omega * tau)

    phi = (beta0 / omega) * (
        omega * tau - zeta * np.sin(omega * tau)
    )

    x = r * np.cos(phi)
    y = r * np.sin(phi)

    print("\nPerturbed circular-orbit parameters")
    print(f"B = {B}")
    print(f"e = {e}")
    print(f"r0 = {r0}")
    print(f"epsilon = {epsilon}")
    print(f"L = {L:.10f}")
    print(f"E^2 = {E_squared:.10f}")
    print(f"E = {E:.10f}")
    print(f"omega = {omega:.10f}")
    print(f"beta0 = {beta0:.10f}")
    print(f"omega / abs(beta0) = {omega / abs(beta0):.4f}")
    print(f"zeta = {zeta:.10f}")
    print(f"Angular integration time = {tau_end:.4f}")
    print(f"Radial periods covered = {num_radial_periods}")

    return x, y


# ============================================================
# Part 3: Run both cases
# ============================================================

x_weak, y_weak = simulate_weak_field()

x_perturbed, y_perturbed = simulate_perturbed_circular_orbit(
    B=0.1,
    e=18.068,
    r0=6.0,
    epsilon=0.01,
)


# ============================================================
# Part 4: Plot
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Weak-field hypocycloid
axes[0].plot(x_weak, y_weak, linewidth=0.8)
axes[0].set_title("Weak-field hypocycloid: B = 0.001")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].set_aspect("equal", adjustable="box")
axes[0].grid(True, alpha=0.3)

# Perturbed circular orbit
axes[1].plot(x_perturbed, y_perturbed, linewidth=0.8)
axes[1].set_title(
    "Perturbed circular orbit: B = 0.1, e = 18.068"
)
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].set_aspect("equal", adjustable="box")
axes[1].grid(True, alpha=0.3)

# Zoom in around the circular orbit at r0 = 6
axes[1].set_xlim(5.7, 6.3)
axes[1].set_ylim(-0.3, 0.3)

plt.tight_layout()
plt.show()
