---
title: "LUT查表reference"
date: 2026-04-03
layout: post
categories: [学习]
tags: [学习]
math: true  # 确保开启数学公式支持
---

> 分析日期：2026年04月03日 | 分析者：[ppdog]

### LUT查表reference
需求：
已知输入数据是float x；非线性计算得到float y = func(x)

#### 量化
1. 量化值 x1 = x / pow(2, qin)
举例： 
in_scale = 0.0625 = pow(2, -4)
out_scale = 0.00390625 = pow(2, -8)
qin = -4, qout = -8

### 查表输入输出qfactor和范围
比如 input data range: （1/32， 32）
output data range: （1/32， 32）
in_qfactor: 9, out_qfactor: 10

### 用onnx模拟过程：
float x  -> Div -> Mul -> Floor -> Clip -> Cast -> 
Gather->
Cast -> Add -> Clip -> Mul -> Floor ->
Clip -> Mul -> float y

### 原理分解
1. 量化： x1 = x / pow(2, qin)
2. 对齐到查表的输入：x2 = x1 * pow(2, in_qfactor + qin)
3. Floor + Clip + Cast： [-32768, 32767]   这里查表是INT16
4. 查表：Gather实现, 得到 x4
5. Add: x5 = x4 + 0.5/pow(2, -qout - out_qfactor)
6. 从查找表对齐到原输出： x6 = x5 * pow(2, -qout - out_qfactor)
7. 反量化回float y = x6 * pow(2, qout)


### 根据查找表范围，调整：
因为查找表的输入有范围：比如 input data range: （1/32， 32）
而我们直接量化的时候，x1可能是int8 [-128,127] uint8 [0,255]
跟查找表的输入范围不一致，导致超出的部分全是边界值。

为此， 我们需要调整到查找表的输入范围。
1. 量化： x1 = x / pow(2, qin)
2. 调整输入范围： x11 = x1 / pow(2, adjustIn) 
   x1 = x11
3. 对齐到查表的输入：x2 = x1 * pow(2, in_qfactor + qin)
4. Floor + Clip + Cast： [-32768, 32767]   这里查表是INT16
5. 查表：Gather实现, 得到 x4
6. Add: x5 = x4 + 0.5/pow(2, -qout - out_qfactor)
7. 从查找表对齐到原输出： x6 = x5 * pow(2, -qout - out_qfactor)
8. 调整输出范围：x61 = x6 * pow(2, adjustOut)
   x6 = x61
9. 反量化回float y = x6 * pow(2, qout)

备注：ajustIn, ajustOut是根据算子情况决定的。
比如reciprocal 算子， adjustIn = -1， adjustOut = 1。
简答介绍下原理：
如果要计算x的倒数，x = 100, y=1/100
调整下：x1 = 100/pow(2, -1), y1 = pow(2, -1)/100
恢复到原始结果：y = y1 * pow(2, 1)
 
