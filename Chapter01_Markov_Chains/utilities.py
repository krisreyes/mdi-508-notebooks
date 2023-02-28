import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

COLORS = ['#242482', '#F00D2C', '#0071BE', '#4E8F00', '#553C67', '#DA5319']

def init(use_latex=False):
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['axes.linewidth'] = 2
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['font.size'] = 14
    mpl.rcParams['legend.fontsize'] = 10
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['figure.facecolor'] = 'white'
    mpl.rcParams['font.sans-serif'] = ['Helvetica Neue', 'Helvetica', 'Tahoma']
    mpl.rcParams['text.usetex'] = use_latex # Set to False if you do not have LaTeX installed
    plt.rc('axes', prop_cycle=cycler(color=COLORS))