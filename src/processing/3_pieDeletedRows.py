import numpy as np
import matplotlib.pyplot as plt

path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/reports/figures/PieDeletedRows.pdf"

labels = [str(round((12161/12317)*100, 2)) + '% - Remaining', str(round((82/12317)*100, 2)) + '% - Invalid rows', str(round((71/12317)*100, 2)) + '% - Missing-Value Threshold Selection']
sizes = [(12161/12317)*100, (82/12317)*100, (71/12317)*100]  
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] 

# Create pie chart
plt.figure(figsize=(8.5,4.5))
plt.pie(
    sizes,
    labels=None,
    colors=colors,
    startangle=90
)
plt.legend(labels, loc="center left", bbox_to_anchor=(0.88889, 0.5))
plt.axis('equal')  
plt.tight_layout() 

plt.savefig(path)
plt.show()