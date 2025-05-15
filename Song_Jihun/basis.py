import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from setuptools.command.rotate import rotate

font_path = "C:/Users/Playdata2/AppData/Local/Microsoft/Windows/Fonts/D2Coding-Ver1.3.2-20180524-all.ttc"		# OS 의 폰트 경로
font_prop = fm.FontProperties(fname=font_path)	# 경로에서 폰트를 불러옴
font_name = font_prop.get_name()				# 폰트명

matplotlib.rc('font', family=font_name)
plt.rc('axes', unicode_minus=False)		# 도표에서 마이너스(-) 를 출력할 때 unicode 를 안쓰게.