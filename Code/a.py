#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# LYS
# 2020/7/5 9:36
# Pachong
# a.py

from IPython.core.pylabtools import figsize
# IPython.core.pylabtools.figsize(sizex, sizey)

import numpy as np
from matplotlib import pyplot as plt
import pymc3 as pm


figsize(12.5, 3.5)  # set figure size
#x y data are in 1.csv
y=[26,
 78,
 80,
 46,
 30,
 16,
 26,
 12,
 8,
 18,
 22,
 10,
 14,
 12,
 12,
 12,
 10,
 22,
 14,
 12,
 6,
 8,
 4,
 14,
 20,
 10,
 2,
 12,
 14,
 10,
 8,
 10,
 10,
 2,
 8,
 14,
 14,
 14,
 10,
 8,
 2,
 8,
 8,
 8,
 6,
 16,
 8,
 12,
 12,
 16,
 16,
 6,
 10,
 4,
 4,
 2,
 10,
 6,
 2,
 10,
 2,
 14,
 14,
 8,
 8,
 22,
 8,
 10,
 6,
 14,
 10,
 2,
 12,
 4,
 6,
 14,
 8,
 8,
 6,
 6,
 2,
 4,
 4,
 2,
 6,
 6,
 8,
 10,
 4,
 4,
 10,
 8,
 4,
 6,
 6,
 8,
 6,
 10,
 8,
 8,
 4,
 4,
 6,
 8,
 2,
 4,
 2,
 4,
 2,
 4,
 4,
 2,
 4,
 4,
 4,
 4,
 6,
 8,
 2,
 2,
 12,
 8,
 16,
 14,
 18,
 12,
 6,
 8,
 10,
 6,
 4,
 4,
 4,
 4,
 2,
 6,
 2,
 4]
x=[]

n_count_data = len(y)
plt.bar(np.arange(n_count_data), y, color="#348ABD")  # 画柱状图
plt.xlabel("Time (days)")
plt.ylabel("count of text-msgs received")
plt.title("Did the user's texting habits change over time?")
plt.xlim(0, 140)  # 设置参数范围,图像所显示x轴的长度
plt.show()

Y=np.array(y)
with pm.Model() as model:
    alpha = 1.0 / Y.mean()  # Recall count_data is the variable that holds our txt counts
    lambda_1 = pm.Exponential("lambda_1", alpha)
    lambda_2 = pm.Exponential("lambda_2", alpha)

    tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data)
    # 产生参数λ1、λ2、τ、α。其中λ1、λ2由机器随机产生，在训练过程中找到更优的τ值。

    with model:
        idx = np.arange(n_count_data)  # Index
        lambda_ = pm.math.switch(tau >= idx, lambda_1, lambda_2)
        # The switch() function assigns lambda_1 or lambda_2 as the value of lambda_, depending on what side of tau we are on.
        # The values of lambda_ up until tau are lambda_1 and the values afterwards are lambda_2.
        # tau, lambda_1, lambda_2 are random, lambda_ will be random. we are not fixing any variables yet!

        observation = pm.Poisson("obs", lambda_, observed=Y)
        #创建模型实例

        step = pm.Metropolis()
        trace = pm.sample(10000, tune=5000, step=step)
        #对后验分布进行10000次采样，指定采样器pm.Metropolis()，turn要调整的迭代次数（如果适用）（默认为无）

        lambda_1_samples = trace['lambda_1']
        lambda_2_samples = trace['lambda_2']
        tau_samples = trace['tau']
        #采样值存储在trace对象中，trace对象是一个字典


figsize(12.5, 10)
# histogram of the samples:

ax = plt.subplot(311)
# subplot(numRows, numCols, plotNum)
# 图表的整个绘图区域被分成 numRows 行和 numCols 列plotNum 参数指定创建的 Axes 对象所在的区域numRows,numCols和plotNum这三个数都小于10的话,可以把它们缩写为一个整数,
# 例如 subplot(323) 和 subplot(3,2,3) 是相同的.

ax.set_autoscaley_on(False)
plt.hist(lambda_1_samples, histtype='stepfilled', bins=30, alpha=0.85,
         label="posterior of $\lambda_1$", color="#A60628", density=True)
#density=True归一化；bins=30 30个箱子，即柱子；histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional(选择展示的类型,默认为bar)

plt.legend(loc="upper left")
plt.title(r"""Posterior distributions of the variables $\lambda_1,\;\lambda_2,\;\tau$""")
plt.xlim([10,20])
plt.xlabel("$\lambda_1$ value")

ax = plt.subplot(312)
ax.set_autoscaley_on(False)
plt.hist(lambda_2_samples, histtype='stepfilled', bins=30, alpha=0.85,
         label="posterior of $\lambda_2$", color="#7A68A6", density=True)
plt.legend(loc="upper left")
plt.xlim([0,10])
plt.xlabel("$\lambda_2$ value")

plt.subplot(313)
w = 1.0 / tau_samples.shape[0] * np.ones_like(tau_samples)  #归一化
plt.hist(tau_samples, bins=n_count_data, alpha=1, label=r"posterior of $\tau$", color="#467821", weights=w, rwidth=2.)
plt.xticks(np.arange(n_count_data))

plt.legend(loc="upper left")
plt.ylim([0, .75])
plt.xlim([60,80])
plt.xlabel(r"$\tau$ (in days)")
plt.ylabel("probability")
plt.show()


figsize(12.5, 5)
N = tau_samples.shape[0]
expected_texts_per_day = np.zeros(n_count_data)
for day in range(0, n_count_data):
    ix = day < tau_samples
    expected_texts_per_day[day] = (lambda_1_samples[ix].sum()
                                   + lambda_2_samples[~ix].sum()) / N

plt.plot(range(n_count_data), expected_texts_per_day, lw=4, color="#E24A33",
         label="expected number of news received")
plt.xlim(0, n_count_data)
plt.xlabel("Day")
plt.ylabel("Expected # news")
plt.title("Expected number of news received")
plt.ylim(0, 60)
plt.bar(np.arange(len(Y)), Y, color="#348ABD", alpha=0.65,
        label="observed news per day")

plt.legend(loc="upper left")
xxx = [i for i in range(0, 140, 30)]
yyy = np.linspace(0, 0, 5)
plt.plot(xxx, yyy, color="r", linestyle="None", marker="*", linewidth=1.0)
plt.show()


#####################
