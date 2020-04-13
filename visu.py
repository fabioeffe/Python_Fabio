import matplotlib
import matplotlib.pyplot as plt
print (matplotlib.__version__)
print(plt.style.available)

plt.style.use('ggplot')

x = ['Apple','Samsung','Huawei','Nokia']
no = [2,4,5,1]

x_pos = [i for i, _ in enumerate (x)]

plt.bar(x_pos, no, color='green')
plt.xlabel("Phone company".title())
plt.ylabel("phones sold (millions)")
plt.title("Phones osld by companies".title())

plt.xticks(x_pos,x)
plt.show()

