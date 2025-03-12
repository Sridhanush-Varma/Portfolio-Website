
import matplotlib.pyplot as plt

labels= ['A Grade Students', 'B Grade Students', 'Failures', 'O Grade Students']

colors=['blue', 'yellow', 'green', 'orange']

sizes= [1500, 600, 500, 300]

plt.pie(sizes,labels=labels, colors=colors, startangle=90, autopct='%2.2f%%')

plt.axis('equal')

plt.show()
