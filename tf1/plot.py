
# coding: utf-8

# In[1]:

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import pickle

# In[2]:

fig = plt.figure()
#ax1 = fig.add_subplot(111, projection='3d')


# In[3]:

#x = [1,2,3,4]
#y = [2,67,3,2]
#z = [4,6,9,2]


# In[4]:

#ax1.plot_wireframe(x, y, z)


# In[6]:

#x = [-1,-2,-3,-4]
#y = [-2,-67,-3,-2]
#z = [4,6,9,2]


# In[5]:

# ax1.set_xlabel('x ax')
# ax1.set_ylabel('y ax')
# ax1.set_zlabel('z ax')
# plt.show()


# In[3]:

#import pickle
f = open('js_crossed_que_vecs.pickle','rb') 
js = pickle.load(f)


# In[4]:

type(js)


# In[5]:

print(js[0])


# In[6]:

f = open('c_crossed_que_vecs.pickle', 'rb')
cp = pickle.load(f)
print(cp[0])


# In[7]:

js_x = [js[i][0] for i in range(len(js))]
js_y = [js[i][1] for i in range(len(js))]
js_z = [js[i][2] for i in range(len(js))]


# In[8]:

cp_x = [cp[i][0] for i in range(len(cp))]
cp_y = [cp[i][1] for i in range(len(cp))]
cp_z = [cp[i][2] for i in range(len(cp))]


# In[9]:

graph = fig.add_subplot(111, projection='3d')


# In[10]:

graph.scatter(js_x, js_y, js_z, c='g', marker='o')
graph.scatter(cp_x, cp_y, cp_z, c='r', marker='o')


# In[11]:

graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')
plt.show()


# In[ ]:



