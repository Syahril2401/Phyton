import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Setup figure dan axis dengan kualitas tinggi
plt.rcParams['figure.dpi'] = 100
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(-12, 12)
ax.set_ylim(-10, 14)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#000011')  # Biru gelap untuk malam

# Warna-warna romantis yang lebih halus
colors = ['#FF69B4', '#FF1493', '#DC143C', '#FF6347', '#FFB6C1', '#FFC0CB', '#DDA0DD', '#DA70D6']

class SmoothFlower:
    def __init__(self, x, y, size=1, bloom_start=0):
        self.x = x
        self.y = y
        self.size = size
        self.bloom_start = bloom_start
        self.petals = []
        self.center_color = '#FFD700'
        self.growth = 0
        self.rotation = 0
        self.pulse = 0
        
    def create_petals(self, frame):
        if frame >= self.bloom_start:
            progress = (frame - self.bloom_start) / 80.0
            self.growth = min(1 - (1 - progress) ** 3, 1.0) if progress <= 1 else 1.0
            
        self.rotation += 0.01
        self.pulse = 0.1 * np.sin(frame * 0.1)
        
        self.petals = []
        for i in range(12):
            angle = i * np.pi / 6 + self.rotation
            petal_size = (self.size + self.pulse) * self.growth
            
            t = np.linspace(0, 2*np.pi, 150)
            heart_x = 16 * np.sin(t)**3
            heart_y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            
            variation = 0.8 + 0.4 * np.sin(i * 0.5)
            heart_x *= variation
            heart_y *= variation
            
            scale = petal_size * 0.08
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            
            x_rot = heart_x * cos_a - heart_y * sin_a
            y_rot = heart_x * sin_a + heart_y * cos_a
            
            petal_x = x_rot * scale + self.x
            petal_y = y_rot * scale + self.y
            
            self.petals.append((petal_x, petal_y, i))
    
    def draw(self, ax, frame):
        self.create_petals(frame)
        for i, (px, py, petal_id) in enumerate(self.petals):
            color = colors[petal_id % len(colors)]
            alpha = 0.8 * self.growth
            for layer in range(3):
                layer_alpha = alpha * (0.3 + 0.7 * (2 - layer) / 2)
                layer_width = 2 - layer * 0.5
                ax.plot(px, py, color=color, linewidth=layer_width, alpha=layer_alpha)
            ax.fill(px, py, color=color, alpha=alpha * 0.2)
        
        if self.growth > 0.3:
            center_size = 40 * self.growth * (1 + self.pulse)
            for layer in range(4):
                size = center_size * (1 + layer * 0.3)
                alpha = 0.8 / (layer + 1)
                ax.scatter(self.x, self.y, s=size, c=self.center_color, 
                          alpha=alpha, edgecolors='orange', linewidth=0.5)

class SmoothHeart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-0.05, 0.05)
        self.vy = random.uniform(0.08, 0.2)
        self.size = random.uniform(8, 25)
        self.alpha = 1.0
        self.rotation = 0
        self.color = random.choice(['#FF69B4', '#FF1493', '#DC143C', '#FFB6C1'])
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.001
        self.alpha -= 0.008
        self.size *= 0.999
        self.rotation += 0.02
        
    def draw(self, ax):
        if self.alpha > 0:
            t = np.linspace(0, 2*np.pi, 120)
            heart_x = 16 * np.sin(t)**3
            heart_y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            
            cos_r, sin_r = np.cos(self.rotation), np.sin(self.rotation)
            heart_x_rot = heart_x * cos_r - heart_y * sin_r
            heart_y_rot = heart_x * sin_r + heart_y * cos_r
            
            scale = self.size * 0.008
            hx = heart_x_rot * scale + self.x
            hy = heart_y_rot * scale + self.y
            
            for layer in range(2):
                layer_alpha = self.alpha * (0.5 + 0.5 * (1 - layer))
                ax.plot(hx, hy, color=self.color, linewidth=1.5 - layer*0.5, alpha=layer_alpha)
            
            ax.fill(hx, hy, color=self.color, alpha=self.alpha*0.3)

class TwinkleStar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.uniform(3, 12)
        self.alpha = random.uniform(0.2, 1.0)
        self.twinkle_speed = random.uniform(0.03, 0.08)
        self.twinkle_phase = random.uniform(0, 2*np.pi)
        self.color = random.choice(['white', '#FFD700', '#FFF8DC', '#F0F8FF'])
        
    def update(self, frame):
        self.alpha = 0.3 + 0.7 * (np.sin(frame * self.twinkle_speed + self.twinkle_phase) + 1) / 2
        
    def draw(self, ax):
        for layer in range(3):
            size = self.size * (1 + layer * 0.5)
            alpha = self.alpha / (layer + 1)
            ax.scatter(self.x, self.y, s=size, c=self.color, alpha=alpha, 
                      marker='*', edgecolors='none')

flowers = [
    SmoothFlower(0, -3, 2.0, 0),
    SmoothFlower(-5, -2, 1.3, 40),
    SmoothFlower(5, -2, 1.3, 45),
    SmoothFlower(-3, 0, 1.0, 80),
    SmoothFlower(3, 0, 1.0, 85),
    SmoothFlower(-1, 2, 0.8, 120),
    SmoothFlower(1, 2, 0.8, 125),
]

hearts = []
stars = [TwinkleStar(random.uniform(-12, 12), random.uniform(4, 14)) for _ in range(50)]

def animate(frame):
    # Gandakan frame untuk menggandakan kecepatan animasi
    fast_frame = frame * 2

    ax.clear()
    ax.set_xlim(-12, 12)
    ax.set_ylim(-10, 14)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#000011')
    
    for star in stars:
        star.update(fast_frame)
        star.draw(ax)
    
    for flower in flowers:
        flower.draw(ax, fast_frame)
        
    if fast_frame > 60 and random.random() < 0.25:
        x = random.uniform(-10, 10)
        y = random.uniform(-8, -3)
        hearts.append(SmoothHeart(x, y))
    
    hearts_to_remove = []
    for heart in hearts:
        heart.update()
        if heart.alpha <= 0 or heart.y > 15:
            hearts_to_remove.append(heart)
        else:
            heart.draw(ax)
    for heart in hearts_to_remove:
        hearts.remove(heart)
    
    if fast_frame > 150:
        alpha = min((fast_frame - 150) / 80.0, 1.0)
        for offset in [(0,0), (0.1,0.1), (-0.1,0.1)]:
            text_alpha = alpha * (0.8 if offset == (0,0) else 0.3)
            ax.text(0 + offset[0], 10 + offset[1], "🌹 Love Blooms Eternal 🌹",
                    fontsize=22, ha='center', va='center',
                    color='#FF69B4', alpha=text_alpha, weight='bold')
            ax.text(0 + offset[0], 8 + offset[1], "In Every Heart, Forever",
                    fontsize=18, ha='center', va='center',
                    color='#FFB6C1', alpha=text_alpha, style='italic')
    
    if fast_frame < 200:
        progress = fast_frame / 200.0
        ax.text(-11, -9, f"✨ {progress*100:.0f}%", fontsize=10, color='white', alpha=0.5)

anim = animation.FuncAnimation(fig, animate, frames=600, interval=10, repeat=True, blit=False)

plt.tight_layout()
plt.show()