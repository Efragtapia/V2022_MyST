#Libraries
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.keys()
import pandas as pd

#Functions
import functions as ft
import numpy as np
import data as dt
import visualizations

def APTgraph(df: pd.DataFrame = None) -> True:
    """
    APT Experiment B Type graph.
    Plots Stacked Bars for each minute, displays in different colors the succesful martingale
    prediction and the unsuccesful, one for each minute of trade.
    
    """
    
    fig = go.Figure(
        data = [
            go.Bar(
                name = "Succesful",
                x = np.arange(0,61),
                y = df["e1"],
                offsetgroup=0,
                text = df["e1"]
            ),
            go.Bar(
                name = "Unsuccesful",
                x = np.arange(0,61),
                y = df["e2"],
                offsetgroup=0,
                base = df["e1"],
                text = df["e2"]
            )
        ]
    )
    
    fig.update_layout(
        xaxis_title = "Minute",
        yaxis_title = "Martingale Count",
        legend_title = "Martingale Prediction",
        title = "Asset Pricing Theory, Experiment C"
    )
    return fig

def APT_graph_w(df: pd.DataFrame = None) -> True:
    """
    APT Experiment C Type graph.
    Plots Stacked Bars for each minute, displays in different colors the succesful martingale
    prediction and the unsuccesful, one for each minute of trade.
   
    """
    
    fig = go.Figure(
        data = [
            go.Bar(
                name = "Succesful",
                x = np.arange(0,61),
                y = df["e1"],
                offsetgroup=0,
                text = df["e1"]
            ),
            go.Bar(
                name = "Unsuccesful",
                x = np.arange(0,61),
                y = df["e2"],
                offsetgroup=0,
                base = df["e1"],
                text = df["e2"]
            )
        ]
    )
    
    fig.update_layout(
        xaxis_title = "Minute",
        yaxis_title = "Martingale Count",
        legend_title = "Martingale Prediction",
        title = "Asset Pricing Theory, Experiment C (Weighted Mid Prices)"
    )
    return fig
    

def Model2_TS_observed(df: pd.DataFrame = None) -> True:
    """
    Plots Line plot comparing actual spread vs calculated spread and histogram showing
    the distribution of the spread.
    
    """
    fig = go.Figure(
        data = [
            go.Scatter(
                x = df.index,
                y = df["Bid"],
                name = "Bid"                
            ),
            go.Scatter(
                x = df.index,
                y = df["Mid"],
                name = "Mid Price"
            ),
            go.Scatter(
                x = df.index,
                y = df["Ask"],
                name = "Ask"
            )
        ]
    )
    fig.update_layout(
        xaxis_title = "Time",
        yaxis_title = "Observed Price",
        legend_title = "Observed",
        title = "Roll Model Prices "
    )
    return fig

def Model2_TS_Theoretical(df: pd.DataFrame = None) -> True:
    """
    Plots Line plot comparing actual spread vs calculated spread and histogram showing
    the distribution of the spread.
    
    """
    fig = go.Figure(
        data = [
            go.Scatter(
                x = df.index,
                y = df["Calc Bid"],
                name = "Theoretical Bid"                
            ),
            go.Scatter(
                x = df.index,
                y = df["Mid"],
                name = "Mid Price"
            ),
            go.Scatter(
                x = df.index,
                y = df["Calc Ask"],
                name = "Theoretical Ask"
            )
        ]
    )
    fig.update_layout(
        xaxis_title = "Time",
        yaxis_title = "Theoretical Price",
        legend_title = "Theoretical",
        title = "Roll Model Theorical"
    )
    return fig
