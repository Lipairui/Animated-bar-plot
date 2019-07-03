import pandas as pd
import holoviews as hv
%load_ext holoviews.ipython
df = pd.read_csv('data.csv')
bars = []
time = df['Year'].unique()
for t in time:
    bar = hv.Bars(df[df['Year']==t])
    bars.append((t,bar))
hmap = hv.HoloMap(bars,'Year').opts(aspect=1, fig_inches=6)
res = hv.output(hmap, holomap='gif', fps=3)
