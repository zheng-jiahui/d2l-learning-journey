#!/usr/bin/env python3
import os
import re
from pathlib import Path

# 定义章节和对应的完成标志
chapters = {
    "02_preliminaries": "预备知识",
    "03_linear_networks": "线性神经网络",
    "04_multilayer_perceptrons": "多层感知机",
    "05_deep_learning_computation": "深度学习计算",
    "06_convolutional_neural_networks": "卷积神经网络",
    "07_modern_cnn": "现代卷积神经网络",
    "08_recurrent_neural_networks": "循环神经网络",
    "09_modern_rnn": "现代循环神经网络",
    "10_attention": "注意力机制",
    "11_optimization": "优化算法",
    "12_computational_performance": "计算性能",
    "13_computer_vision": "计算机视觉",
    "14_natural_language_processing": "自然语言处理",
    "15_nlp_advanced": "NLP进阶",
    "16_recommender_systems": "推荐系统",
    "17_generative_adversarial_networks": "生成对抗网络",
    "18_reinforcement_learning": "强化学习"
}

def check_completed(chapter_dir):
    """检查章节是否完成（目录存在且有 .ipynb 文件）"""
    if not Path(chapter_dir).exists():
        return False
    
    # 检查是否有笔记本文件
    ipynb_files = list(Path(chapter_dir).glob("*.ipynb"))
    return len(ipynb_files) > 0

def calculate_progress():
    """计算完成进度"""
    completed = 0
    for chapter_dir in chapters.keys():
        if check_completed(chapter_dir):
            completed += 1
    
    total = len(chapters)
    percentage = int(completed / total * 100)
    return completed, total, percentage

def update_readme(completed, total, percentage):
    """更新 README.md 中的进度"""
    readme_path = "README.md"
    
    if not Path(readme_path).exists():
        print("README.md not found")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新进度徽章
    badge_pattern = r'!\[Progress\]\(https://img\.shields\.io/badge/Progress-\d+%25-[\w]+\)'
    new_badge = f'![Progress](https://img.shields.io/badge/Progress-{percentage}%25-yellow)'
    
    if re.search(badge_pattern, content):
        content = re.sub(badge_pattern, new_badge, content)
    
    # 更新进度表格
    table_pattern = r'(\| 进度 \| .+ \| \d+% \|)'
    new_table = f'| 进度 | {completed}/{total} 章 | {percentage}% |'
    
    if re.search(table_pattern, content):
        content = re.sub(table_pattern, new_table, content)
    
    # 更新进度条
    bar_pattern = r'!\[Progress\]\(https://geps\.dev/progress\?width=\d+&text=\d+%&color=\w+\)'
    bar_length = 20
    filled = int(percentage / 100 * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    new_bar = f'[![{bar}](https://geps.dev/progress?width={bar_length}&text={percentage}%25&color=yellow)]'
    
    if re.search(bar_pattern, content):
        content = re.sub(bar_pattern, new_bar, content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Progress updated: {completed}/{total} ({percentage}%)")

if __name__ == "__main__":
    completed, total, percentage = calculate_progress()
    update_readme(completed, total, percentage)