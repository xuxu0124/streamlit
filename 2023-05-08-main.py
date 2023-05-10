#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: XuXu

# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import graphviz as graphviz
import streamlit as st

st.title('这是title')
st.header('这是header')
st.subheader('这是subheader')
st.caption('这是caption')

# st.text('这是第一段text文字\n前面加了回车')
# st.text('这是另一段文字')
#
# st.write('这是用write打出来的')
#
# st.markdown('# markdown打出来1个#号')
# st.markdown('## markdown打出来2个#号')
# st.markdown('### markdown打出来3个#号')
# st.markdown('# 带了符号 I ***Love*** You')
#
# st.latex('a^2 + b^2 = 1')
#
# code = '''
# def func(a_in, b_in):
#     return a + b
#
# a = 1
# b = 2
# print(func(a, b))
# '''
# st.code(code, language='python')
#
# nr, nc = 30, 20
# df = pd.DataFrame(np.random.randn(nr, nc), columns=['某列数据col_{:02}'.format(i) for i in range(nc)])
# st.dataframe(df.style.highlight_max(axis=0))

# 地图不能显示
# df = pd.DataFrame(dict(longitude=[113, 116.5], latitude=[23.5, 40]))
# df = pd.DataFrame(
#     np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
#     columns=['latitude', 'longitude']
# )
# st.map(df)

# st.graphviz_chart('''
#     digraph {
#         "Training Data" -> "ML Algorithm"
#         "ML Algorithm" -> "机器学习模型"
#         "机器学习模型" -> "Result Forecasting"
#         "New Data" -> "机器学习模型"
#     }
# ''')

# from plotnine import ggplot, aes, geom_tile, geom_text, scale_fill_cmap, coord_equal, theme, element_text
#
# nr, nc = 100, 10
# df_data = pd.DataFrame(np.random.randn(nr, nc), columns=['col_{:>02d}'.format(i) for i in range(nc)])
# df_data = (
#     df_data.corr().
#     round(2).
#     reset_index().
#     rename(columns={'index': '第i个特征'}).
#     melt(id_vars='第i个特征', var_name='第j个特征', value_name='corr')
# )
# plot_temp = (
#     ggplot(df_data, aes(x='第i个特征', y='第j个特征', fill='corr')) +
#     geom_tile(color='white') +
#     geom_text(aes(label='corr'), size=6, color='grey') +
#     scale_fill_cmap('RdBu_r') +
#     coord_equal() +
#     theme(
#         dpi=300, figure_size=(10, 10),
#         text=element_text(family='Microsoft YaHei'),
#         axis_text_x=element_text(angle=90)
#     )
# )
# st.pyplot(ggplot.draw(plot_temp))
