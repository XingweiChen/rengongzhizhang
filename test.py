import tensorflow as tf
import numpy as np
import time
from tensorflow.python import debug as tf_debug

k_true = [[1, -1], [3, -3], [2, -2]]
b_true = [-5, 5]
num_examples = 120


def model(inputs):
    #define model architecture, loss and training operator
    y_hat = tf.layers.dense(inputs[0], units=2)
    loss = tf.reduce_mean(
        tf.losses.mean_squared_error(inputs[1], y_hat), name='loss')
    train_op = tf.train.GradientDescentOptimizer(0.05).minimize(loss)
    return y_hat, loss, train_op

sess = tf.Session()
# sess = tf_debug.TensorBoardDebugWrapperSession(sess, "brook-Lenovo-Rescuer-15ISK:7000")
num_of_instance = 50
xs = np.random.randn(num_of_instance, num_examples, 3)
ys = np.matmul(xs, k_true) + b_true

dx = tf.data.Dataset.from_tensor_slices(xs)
dy = tf.data.Dataset.from_tensor_slices(ys)
train_dataset = tf.data.Dataset.zip((dx, dy)).shuffle(500).repeat().batch(30)
iterator = train_dataset.make_initializable_iterator()


# extract an element
next_element = iterator.get_next()
y_hat, loss, train_op = model(next_element)

training_init_op = iterator.make_initializer(train_dataset)
init_op = tf.global_variables_initializer()
sess.run(init_op)
sess.run(training_init_op)
tf.summary.scalar('loss', loss)
tf.summary.histogram('y_hat', y_hat)
merged = tf.summary.merge_all()
summary_writer = tf.summary.FileWriter('logdir/' + str(time.time()),
                                  sess.graph)
for i in range(50):
    summary, loss_val, _ = sess.run([merged, loss, train_op])
    # loss_val, _ = sess.run([loss, train_op])
    print("Iteration %d: loss = %g" % (i, loss_val))

    summary_writer.add_summary(summary, i)

sess.close()
