# 2次元のグラフを作成するプログラム

# モジュール
import numpy as np
import matplotlib.pyplot as plt # グラフ描画
import matplotlib.cm as cm      # グラフのカラーマップ
import matplotlib.ticker as mt  # グラフの目盛

# mplstyleの読み込み
plt.style.use('./thesis.mplstyle')

# ////////////////////make figure////////////////////
fig, ax = plt.subplots(1, 1)
# --------------------[setting]--------------------
# 関数の定義
def decimal_normalize(value) :
    if isinstance(value, float) and value.is_integer() :
        return int(value)
    return value

# ラベル等
figure_filename = 'test'    # 画像ファイルの名前
wdir_path       = './'        # 保存するディレクトリのパス
file_extension  = 'pdf'         # 画像ファイルの形式
title           = None          # グラフのタイトル
xaxis_label     = r'$xlabel$' # x軸のラベル
yaxis_label     = r'$ylabel$' # y軸のラベル

# プロット範囲
# x軸
plot_xmin = None # 下限
plot_xmax = None # 上限
# plot_xmin = None # 下限
# plot_xmax = None # 上限
# y軸
plot_ymin = None # 下限
plot_ymax = None # 上限
# plot_ymin = None # 下限
# plot_ymax = None # 上限

# 対数スケール
flag_log_xaxis = False # x軸
flag_log_yaxis = False # y軸
# flag_log_xaxis = True # x軸
# flag_log_yaxis = True # y軸

# 軸目盛の最適化
flag_edit_xaxis  = 'optimize' # x軸
flag_edit_yaxis  = 'optimize' # y軸
# flag_edit_xaxis  = 'manual' # x軸
# flag_edit_yaxis  = 'manual' # y軸
# flag_edit_xaxis  = None # x軸
# flag_edit_yaxis  = None # y軸
list_xticks      = []
list_xtickslabel = []
list_yticks      = []
list_ytickslabel = []

# --------------------[plotting]--------------------
x = np.array([i for i in range(1, 10)])
y = x**2
ax.plot(x, y)

# --------------------[processing]--------------------
# タイトル
if title != None : 
    ax.set_title(title)

# 軸ラベル
if xaxis_label != None : 
    ax.set_xlabel(xaxis_label)
if yaxis_label != None :
    ax.set_ylabel(yaxis_label)

# logスケール
if flag_log_xaxis : 
    ax.set_xscale('log')
if flag_log_yaxis :
    ax.set_yscale('log')

# プロット範囲
if plot_xmin != None and plot_xmax != None :
    ax.set_xlim(plot_xmin, plot_xmax)
if plot_ymin != None and plot_ymax != None :
    ax.set_ylim(plot_ymin, plot_ymax)

# 軸目盛ラベル
if flag_edit_xaxis == 'manual' :
    ax.set_xticks(list_xticks)
    ax.set_xticklabels(list_xtickslabel)
elif flag_edit_xaxis == 'optimize':
    ax.xaxis.set_minor_formatter(mt.NullFormatter()) # マイナー目盛の表示を抑制
    list_xticks_info = ax.get_xticklabels()          # x軸目盛の全情報を取得
    print(f'x軸の目盛の情報：{list_xticks_info}')
    list_xticks = [list_xticks_info[i].get_position()[0] for i in range(len(list_xticks_info))] # 目盛の位置を取得
    list_xticklabels = [list_xticks_info[i].get_text() for i in range(len(list_xticks_info))] # 目盛の文字列を取得
    list_xticklabels_formatted = []
    for i in range(len(list_xticklabels)) :
        text_trimmed = list_xticklabels[i].replace('$\mathdefault{', '').replace('}$', '').replace('−', '-')
        if text_trimmed.find('^') == -1 : # 指数表記ではない場合，末尾の余分な0を消す
            text_trimmed = '$' + str(decimal_normalize(float(text_trimmed))) + '$'
        else : # 指数表記の場合は，10^0と10^1を1と10に直す
            if list_xticks[i] == 1 :
                text_trimmed = '$1$'
            elif list_xticks[i] == 10 :
                text_trimmed = '$10$'
            else :
                text_trimmed = '$' + text_trimmed + '$'
        list_xticklabels_formatted.append(text_trimmed)
    ax.set_xticks(list_xticks)
    ax.set_xticklabels(list_xticklabels_formatted)

if flag_edit_yaxis == 'manual' :
    ax.set_yticks(list_yticks)
    ax.set_yticklabels(list_ytickslabel)
elif flag_edit_yaxis == 'optimize':
    ax.yaxis.set_minor_formatter(mt.NullFormatter()) # マイナー目盛の表示を抑制
    list_yticks_info = ax.get_yticklabels()          # x軸目盛の全情報を取得
    print(f'y軸目盛の情報：{list_yticks_info}')
    list_yticks = [list_yticks_info[i].get_position()[1] for i in range(len(list_yticks_info))] # 目盛の位置を取得
    list_yticklabels = [list_yticks_info[i].get_text() for i in range(len(list_yticks_info))] # 目盛の文字列を取得
    list_yticklabels_formatted = []
    for i in range(len(list_yticklabels)) :
        text_trimmed = list_yticklabels[i].replace('$\mathdefault{', '').replace('}$', '').replace('−', '')
        if text_trimmed.find('^') == -1 : # 指数表記ではない場合，末尾の余分な0を消す
            text_trimmed = '$' + str(decimal_normalize(float(text_trimmed))) + '$'
        else : # 指数表記の場合は，10^0と10^1を1と10に直す
            if list_yticks[i] == 1 :
                text_trimmed = '$1$'
            elif list_yticks[i] == 10 :
                text_trimmed = '$10$'
            else :
                text_trimmed = '$' + text_trimmed + '$'
        list_yticklabels_formatted.append(text_trimmed)
    ax.set_yticks(list_yticks)
    ax.set_yticklabels(list_yticklabels_formatted)

# プロット範囲
if plot_xmin != None and plot_xmax != None : 
    ax.set_xlim(plot_xmin, plot_xmax)
if plot_ymin != None and plot_ymax != None :
    ax.set_ylim(plot_ymin, plot_ymax)

# 図を保存
fig.savefig(fname = wdir_path + figure_filename + '.' + file_extension)