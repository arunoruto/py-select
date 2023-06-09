import numpy as np
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

st.title("Stream Select")

img1 = Image.open('westconcordaerial.png').convert('RGB')
img2 = Image.open('westconcordorthophoto.png').convert('RGB')

# fig1 = go.Figure(
#     go.Image(
#         z = img1
#     )
# )
# fig2 = go.Figure(
#     go.Heatmap(
#         z = img2
#     )
# )
fig1 = px.imshow(img1)
fig2 = px.imshow(img2)

fig1.update_layout(
    hovermode='y',
)

for fig in [fig1, fig2]:
    fig.update_layout(
        xaxis = dict(
            visible=False,
            # showticklabels=False,
        ),
        yaxis = dict(
            visible=False,
        ),
    )

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)