import numpy as np
import matplotlib.pyplot as plt

def regular_ngon(n, R=1.0, center=(0, 0)):
    angles = np.linspace(0, 2*np.pi, n+1)
    x = center[0] + R * np.cos(angles)
    y = center[1] + R * np.sin(angles)
    return x, y

def plot_polygon_roundness_spectrum(
    ns=(3, 4, 5, 6, 8, 12),
    R=1.0,
    save_path="docs/img/roundness-polygons.png"
):
    cols = 3
    rows = int(np.ceil(len(ns) / cols))

    fig, axes = plt.subplots(rows, cols, figsize=(4*cols, 4*rows))
    axes = np.array(axes).reshape(-1)

    for ax, n in zip(axes, ns):
        x, y = regular_ngon(n, R)
        ax.plot(x, y, label=f"n={n}", color="C0")

        circle = plt.Circle((0, 0), R, color="gray",
                            linestyle="--", fill=False, alpha=0.5)
        ax.add_artist(circle)

        ax.set_aspect("equal")
        ax.set_title(f"n = {n}")
        ax.set_xticks([])
        ax.set_yticks([])

    # 余った枠は消す
    for ax in axes[len(ns):]:
        ax.axis("off")

    fig.suptitle("Polygonal Worlds by n (Roundness Spectrum)", fontsize=14)
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)

    if save_path is not None:
        plt.savefig(save_path, dpi=200)
    else:
        plt.show()

if __name__ == "__main__":
    plot_polygon_roundness_spectrum()
