#!/bin/bash
# 每日学习笔记生成脚本

DATE=$(date +%Y-%m-%d)
TODAY="content/posts/$DATE.md"

# 从模板创建
hugo new posts/$DATE.md

# 打开编辑器
code content/posts/$DATE.md

echo "📝 今日笔记已创建: $TODAY"
echo "✍️  开始写今天的笔记吧！"