#Contains the building blocks of the main maodel.
import tensorflow as tf

def embedding_layer(inputs,vocab_size,num_units,zero_pad=True,scope="embedding",reuse=None):
    """This is embedding layer which encodes nums into embedding vectors."""
    with tf.variable_scope(scope,reuse):
        lookup_table=tf.get_variable('lookup_table',dtype=tf.float32,shape=[vocab_size,num_units],
                     initializer=tf.truncated_normal_initializer(mean=0.0,stddev=0.1))
        if zero_pad:
            lookup_table=tf.concat((tf.zeros(shape=[1,num_units]),lookup_table[1:,:]),0)
        outputs=tf.nn.embedding_lookup(lookup_table,inputs)
    return outputs

def normalize(inputs,scope="normalize",reuse=None):
    """Performs normalisation across last axis."""
    return tf.contrib.layers.layer_norm(inputs,begin_norm_axis=-1,scope=scope,reuse=reuse)

def highwaynet(inputs,num_units=None,scope="highwaynet",reuse=None):
    """A highway net for proving scope for training deeper nets efficiently."""

    if not num_units:
        num_units=inputs.get_shape()[-1]
    with tf.variable_scope(scope,reuse=reuse):
        H=tf.layers.dense(inputs,units=num_units,activation=tf.nn.relu,name="dense1")
        T=tf.layers.dense(inputs,units=num_units,activation=tf.nn.sigmoid,bias_initializer=tf.constant_initializer(-1.0),name='dense2')
    return H * T + inputs * (1.0 - T)

def conv_layers(inputs,filters=None,size=1,rate=1,padding="SAME",dropout_rate=0,use_bias=True,
                activation_fn=None,training=None,scope="conv1d",reuse=None):
    """Creates 1D Convolutional layers with normalisation"""

    with tf.variable_scope(scope):
        if padding.lower()=="causal":
            pad_len = (size - 1) * rate
            inputs = tf.pad(inputs, [[0, 0], [pad_len, 0], [0, 0]])
            padding = "valid"
        if filters is None:
            filters=inputs.get_shape().as_list()[-1]
        out=tf.layers.conv1d(inputs=inputs,filters=filters,kernel_size=size,dilation_rate=rate,
                                padding=padding,use_bias=use_bias,kernel_initializer=tf.contrib.layers.variable_scaling_initializer(),
                                reuse=reuse)
        out=normalize(out)
        if activation_fn is not None:
            out=activation_fn(out)
        out=tf.layers.dropout(out,rate=dropout_rate,training=training)
    return out

def highwayconvolution(inputs,filters=None,size=1,rate=1,padding="SAME",dropout_rate=0,use_bias=True,activation_fn=None,
                      training=True,scope="hc",reuse=None):

    """Creates the high convolution layer."""
    former_input=inputs
    with tf.variable_scope(scope):
        if padding.lower()=="casual":
            pad_len=(size-1)*rate
            inputs=tf.pad(inputs,[[0,0],[pad_len,0],[0,0]])
            padding="valid"

        if filters is None:
            filters=inputs.get_shape().as_list()[-1]

        out=tf.layers.conv1d(inputs=inputs,filters=2*filters,kernel_size=size,
                                dilation_rate=rate,padding=padding,use_bias=use_bias,
                                kernel_initializer=tf.contrib.layers.variable_scaling_initializer(),reuse=reuse)
        H1,H2=tf.split(out,2,axis=-1)
        H1=normalize(H1,scope="H1")
        H2=normalize(H2,scope="H2")
        H1=tf.nn.sigmoid(H1,"gate")
        H2=activation_fn(H2,"info") if activation_fn is not None else H2
        out=H1*H2+(1.-H2)*former_input

        out=tf.layers.dropout(out,rate=dropout_rate,training=training)
    return out

def conv_transpose(inputs,filters=None,size=3,stride=2,padding='same',
                   dropout_rate=0,use_bias=True,activation=None,
                   training=True,scope="conv1d_transpose",reuse=None):

    with tf.variable_scope(scope,resue=resue):
        if filters is None:
            filters=inputs.get_shape().as_list()[-1]
        inputs=tf.expand_dims(inputs,1)
        out=tf.layers.conv2d_transpose(inputs,filters=filters,kernel_size=(1,size),
                                          padding=padding,activation=None,kernel_initializer=tf.contrib.layers.variable_scaling_initializer(),
                                          use_bias=use_bias)
        out=tf.squeeze(out,1)
        out=normalize(out)
        if activation is not None:
            out=activation(out)

        out=tf.layer.dropout(out,rate=dropout_rate,training=training)
    return out
