import torch
import torchvision
from torchvision import transforms
from d2l import torch as d2l

# ===================== 1. 定义图像变换 =====================
# 将图片转为 tensor（自动归一化到 [0,1]）
trans = transforms.ToTensor()

# ===================== 2. 加载 FashionMNIST 数据集 =====================
# 训练集
train_data = torchvision.datasets.FashionMNIST(
    root="../data", train=True, transform=trans, download=True)
# 测试集
test_data = torchvision.datasets.FashionMNIST(
    root="../data", train=False, transform=trans, download=True)

# ===================== 3. 查看数据集基本信息 =====================
print("训练集数量：", len(train_data))
print("测试集数量：", len(test_data))
print("单张图片 shape：", train_data[0][0].shape)  # torch.Size([1,28,28])

# ===================== 4. 标签数字 <-> 文本互转 =====================
def get_fashion_mnist_labels(labels):
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
                   'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]

# ===================== 5. 可视化图像 =====================
def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):
    d2l.use_svg_display()
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        ax.imshow(img.numpy().squeeze(), cmap='gray')
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes

# 取一批图片显示
X, y = next(iter(torch.utils.data.DataLoader(train_data, batch_size=18)))
show_images(X, 2, 9, titles=get_fashion_mnist_labels(y))
d2l.plt.show()

# ===================== 6. 批量读取数据（DataLoader） =====================
batch_size = 256

# 多线程加载（Windows 可能需要设 num_workers=0）
train_iter = torch.utils.data.DataLoader(
    train_data, batch_size, shuffle=True, num_workers=0)
test_iter = torch.utils.data.DataLoader(
    test_data, batch_size, shuffle=False, num_workers=0)

# 测试读取速度
timer = d2l.Timer()
for X, y in train_iter:
    continue
print(f'读取全部训练批次耗时：{timer.stop():.2f}s')