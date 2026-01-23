#!/usr/bin/env python3
"""
每日学习笔记自动化脚本
自动创建Markdown、打开编辑器、备份到Git
"""

import os
import sys
from datetime import datetime
import subprocess
import argparse

def create_daily_note(date_str=None):
    """创建今日学习笔记"""
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    # 文件路径
    posts_dir = "content/posts"
    filename = f"{date_str}.md"
    filepath = os.path.join(posts_dir, filename)
    
    # 确保目录存在
    os.makedirs(posts_dir, exist_ok=True)
    
    # 如果文件已存在，询问是否覆盖
    if os.path.exists(filepath):
        choice = input(f"📁 文件已存在，覆盖？(y/N): ")
        if choice.lower() != 'y':
            print("❌ 已取消")
            return filepath
    
    # 创建内容
    content = f"""---
title: "{date_str} 学习笔记"
date: {date_str}
draft: false
categories: ["自动驾驶", "机器人"]
tags: ["daily"]
series: ["每日学习"]
summary: "今日学习自动驾驶/机器人模型记录"
---

# {date_str} 学习记录

## 🎯 今日学习目标
- [ ] 

## 📖 学习内容
### 1. 模型/技术名称：

### 2. 核心原理：

### 3. 关键代码：

## 💡 重点总结

## ❓ 疑难问题

## 🔗 参考资源
1. 
2. 
3. 

---
*本文是自动驾驶/机器人每日学习系列的一部分*
"""
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 笔记已创建: {filepath}")
    return filepath

def open_editor(filepath):
    """用编辑器打开文件"""
    editors = ["code", "sublime_text", "atom"]
    
    for editor in editors:
        try:
            if sys.platform == "win32":
                os.startfile(filepath)
            else:
                subprocess.run([editor, filepath])
            print(f"✍️  用 {editor} 打开笔记")
            return True
        except:
            continue
    
    print("📄 文件位置: " + os.path.abspath(filepath))
    return False

def git_commit(filepath):
    """提交到Git"""
    try:
        subprocess.run(["git", "add", filepath], check=True)
        subprocess.run(["git", "commit", "-m", f"📚 添加{os.path.basename(filepath)}"], check=True)
        print("✅ 已提交到Git")
    except Exception as e:
        print(f"⚠️  Git提交失败: {e}")

def main():
    parser = argparse.ArgumentParser(description="创建每日学习笔记")
    parser.add_argument("--date", help="指定日期 (格式: YYYY-MM-DD)")
    parser.add_argument("--no-edit", action="store_true", help="不打开编辑器")
    parser.add_argument("--auto-commit", action="store_true", help="自动提交到Git")
    
    args = parser.parse_args()
    
    print("📚 自动驾驶/机器人每日学习笔记生成器")
    print("=" * 50)
    
    # 创建笔记
    filepath = create_daily_note(args.date)
    if not filepath:
        return
    
    # 打开编辑器
    if not args.no_edit:
        open_editor(filepath)
    
    # 自动提交
    if args.auto_commit:
        git_commit(filepath)
    
    print("\n🎉 完成！开始今天的学习吧！")

if __name__ == "__main__":
    main()