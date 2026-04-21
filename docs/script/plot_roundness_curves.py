import numpy as np
import matplotlib.pyplot as plt

def alpha_eff(n):
    n = np.asarray(n, dtype=float)
    return (n / np.pi) * np.sin(2 * np.pi / n)

def k_eff(n):
    a = alpha_eff(n)
    return 2 ** (-1.0 / a)

def pi_n(n):
    n = np.asarray(n, dtype=float)
    return n * np.sin(np.pi / n)

def plot_roundness_spectrum_curves(
    n_min=3,
    n_max=60,
    save_path="docs/img/roundness-curves.png"
):
    ns = np.arange(n_min, n_max + 1)

    a_eff = alpha_eff(ns)
    k_e = k_eff(ns)
    pi_vals = pi_n(ns)

    fig, axes = plt.subplots(3, 1, figsize=(6, 10), sharex=True)

    # α_eff(n)
    axes[0].plot(ns, a_eff, color="C0")
    axes[0].axhline(2.0, color="gray", linestyle="--", alpha=0.5)
    axes[0].set_ylabel(r"$\alpha_{\mathrm{eff}}(n)$")
    axes[0].set_title("Roundness Spectrum: α_eff, k_eff, π_n")

    # k_eff(n)
    axes[1].plot(ns, k_e, color="C1")
    axes[1].axhline(2 ** -0.5, color="gray", linestyle="--", alpha=0.5)
    axes[1].set_ylabel(r"$k_{\mathrm{eff}}(n)$")

    # π_n
    axes[2].plot(ns, pi_vals, color="C2")
    axes[2].axhline(np.pi, color="gray", linestyle="--", alpha=0.5)
    axes[2].set_ylabel(r"$\pi_n$")
    axes[2].set_xlabel("n")

    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=200)
    else:
        plt.show()

if __name__ == "__main__":
    plot_roundness_spectrum_curves()
