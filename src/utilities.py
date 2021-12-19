# -*- coding: utf-8 -*-
#  File: utilities.py
#  Project: 'Otus HW1'
#  Created by Gennady Matveev (gm@og.ly) on 18-12-2021.
#  Copyright 2021. All rights reserved.

import pandas as pd
import numpy as np


# seaborn change bar width
def set_bar_width(ax, new_value):
    """
    Change bar width in sns.countplot...

    Args:
        ax (plt.axes): plt axes
        new_value (float): bar width multiplier, < 1

    Expects fig, ax = plt.subplots() before
    Doesn't work on sns plots
    """
    for patch in ax.patches:
        current_width = patch.get_width()
        diff = current_width - new_value

        # Change bar width
        patch.set_width(new_value)

        # Recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

# Add data annotation to plot


def annot_plot(ax, rows):  # w,h,
    """
    Annotates plot data with values

    Args:
        ax (plt.axes): plt axes
        ? w ([type]): [description]
        ? h ([type]): [description]
        rows (int): number of rows in dataframe = df.shape[0]

    Expects fig, ax = plt.subplots() before
    Works on data (array,datframe) with number of rows = rows

    """
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for p in ax.patches:
        ax.annotate(f"{p.get_height()*100/rows:.2f}%", (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=11, color='black', rotation=0, xytext=(0, 10),
                    textcoords='offset points')


def highlight_max_0(df: pd.DataFrame, props='color:orange'): #;background-color: green
    """
    Highlights datafreme cells mith max values

    Args:
        df (pd.DataFrame)
        props (str, optional): colors. Defaults to 'color:white;background-color: green':str.

    Returns:
        [numpy array]: what to do in a cell

    Examples:
        df.apply(highlight_max, axis=0) for columns
        df.apply(highlight_max, axis=1) for rows
    """
    return np.where(df == np.nanmax(df.values), props, '')


def nice_metric_table(df: pd.DataFrame, metric: list) -> pd.DataFrame:
    df1 = pd.DataFrame()
    
    for col in df.columns:
        if col.startswith("time"):
            df.drop(columns=col, inplace=True)
    for c in df.columns:
        df1 = pd.concat([df1, pd.DataFrame([pd.Series(x)
                        for x in df[c]])], axis=1)
    cols = [(init, metr) for init in df.columns for metr in metric]
    
    df1.columns = pd.MultiIndex.from_tuples(cols)
    df1.index = df.index
    # df1 = df1.applymap(lambda x: round(x, 4), na_action='ignore')
    # df1.fillna('-',inplace=True)
    df1.style.highlight_max(props='color:green; font',axis=1)
    # df1.style.apply(highlight_max_0(df1, props='color:green; font'), axis=0)#, subset = pd.IndexSlice[:, pd.IndexSlice[:, metric]])

    return df1
