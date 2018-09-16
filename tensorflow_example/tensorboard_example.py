import tensorflow as tf
import numpy as np
import time


k_true = [[1, -1], [3, -3], [2, -2]]
b_true = [-5, 5]
num_examples = 120


with tf.Session() as sess:
    #input place holders
    x = tf.placeholder(tf.float32, shape=[None, 3], name='x')
    y = tf.placeholder(tf.float32, shape=[None, 2], name='y')

    #define model architecture, loss and training operator
    y_hat = tf.layers.dense(inputs=x, units=2, use_bias=True)
    loss = tf.reduce_mean(
        tf.losses.mean_squared_error(y, y_hat), name='loss')
    train_op = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

    tf.summary.scalar('loss', loss)
    tf.summary.histogram('y_hat', y_hat)
    merged = tf.summary.merge_all()
    summary_writer = tf.summary.FileWriter('logdir/' + str(time.time()),
                                      sess.graph)

    # sess = tf.debug.TensorBoardDebugWrapperSession(sess, "brook:7000")
    sess.run(tf.global_variables_initializer())

    for i in range(50):
        xs = np.random.randn(num_examples, 3)
        ys = np.matmul(xs, k_true) + b_true

        summary, loss_val, _ = sess.run([merged, loss, train_op], feed_dict={x: xs, y:ys})
        print("Iteration %d: loss = %g" % (i, loss_val))

        summary_writer.add_summary(summary, i)
