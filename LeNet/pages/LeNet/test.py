import tensorflow as tf



n0=0
n1=0
x=2








w=tf.Variable(tf.zeros([n0,n1]))
b=tf.Variable(tf.zeros([n1]))
y=tf.nn.softmax(tf.matmul(x,w)+b)