#!/bin/bash
# deploy.sh — EC2 上一键部署 / 更新
# 用法: bash deploy.sh

set -e

echo "==> [1/5] 拉取最新代码..."
git pull origin main

echo "==> [2/5] 检查 .env 文件..."
if [ ! -f .env ]; then
  echo "❌ 找不到 .env 文件！请先复制 .env.docker 并填写真实的 key："
  echo "   cp .env.docker .env && nano .env"
  exit 1
fi

echo "==> [3/5] 构建镜像..."
docker compose build --no-cache

echo "==> [4/5] 启动服务..."
docker compose up -d

echo "==> [5/5] 查看状态..."
docker compose ps
echo ""
echo "✅ 部署完成！"
echo "   后端地址: http://$(curl -s ifconfig.me):8000"
echo "   查看日志: docker compose logs -f backend"
