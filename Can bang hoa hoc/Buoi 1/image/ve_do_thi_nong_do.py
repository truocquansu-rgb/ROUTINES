# Đồ thị nồng độ theo thời gian, đi tới cân bằng từ hai phía (số liệu PX1, Kc = 64, bình 10 L).
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BLUE, ORANGE = '#2a78d6', '#eb6834'
INK, MUTED, GRID = '#1f1f1f', '#6b6b6b', '#d9d9d9'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'text.color': INK,
                     'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': MUTED})

KF, KC = 1.0, 64.0


def simulate(h0, hi0, t_end=4.0, dt=0.001):
    # H2 + I2 <=> 2HI, v_thuận = kf[H2][I2], v_nghịch = (kf/Kc)[HI]^2
    t, h, hi, T, H, HI = 0.0, h0, hi0, [], [], []
    while t <= t_end:
        T.append(t); H.append(h); HI.append(hi)
        r = KF * h * h - KF / KC * hi * hi
        h -= r * dt * 40; hi += 2 * r * dt * 40; t += dt
    return T, H, HI


panels = [('Xuất phát từ H₂ và I₂ (0,15 mol/L mỗi chất)', simulate(0.15, 0.0)),
          ('Xuất phát từ HI (0,30 mol/L)', simulate(0.0, 0.30))]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
for ax, (title, (T, H, HI)) in zip(axes, panels):
    t_eq = next(t for t, h in zip(T, H) if abs(h - 0.03) < 0.0005)
    ax.axvspan(t_eq, T[-1], color='#eef6ee', zorder=0)
    ax.text((t_eq + T[-1]) / 2, 0.285, 'Trạng thái\ncân bằng', ha='center', va='top', color=MUTED, fontsize=10)
    for y in (0.24, 0.03):
        ax.axhline(y, color=GRID, lw=1, ls='--', zorder=1)
    ax.plot(T, HI, color=ORANGE, lw=2, zorder=3)
    ax.plot(T, H, color=BLUE, lw=2, zorder=3)
    ax.text(T[-1], 0.24 + 0.012, 'HI', color=INK, ha='right', fontsize=11)
    ax.text(T[-1], 0.03 + 0.012, 'H₂, I₂', color=INK, ha='right', fontsize=11)
    ax.set_title(title, fontsize=11, color=INK)
    ax.set_xlabel('Thời gian')
    ax.set_xticks([])
    ax.set_xlim(0, T[-1]); ax.set_ylim(0, 0.32)
    ax.set_yticks([0, 0.03, 0.15, 0.24, 0.30])
    ax.set_yticklabels(['0', '0,03', '0,15', '0,24', '0,30'])
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(MUTED)
axes[0].set_ylabel('Nồng độ (mol/L)')

h1, = axes[1].plot([], [], color=ORANGE, lw=2, label='HI')
h2, = axes[1].plot([], [], color=BLUE, lw=2, label='H₂, I₂')
fig.legend(handles=[h1, h2], loc='upper center', ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.02))
fig.tight_layout(rect=(0, 0, 1, 0.93))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'do_thi_nong_do_hai_chieu.png')
fig.savefig(out, dpi=250, facecolor='white'); print(out)
