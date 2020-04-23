#Building the DCTTS model network.

from ModelBuildingBlocks import *
import tensorflow as tf
import Hyperparams as hp



def TextEnc(word,training=True):
    i=1
    out=embedding_layer(vocab_size=len(hp.vocab),num_units=hp.e,scope="embed_{}".format(i))
    i+=1
    out=conv_layers(out,filters=2*hp.d,size=1,rate=1,dropout_rate=hp.dropout_rate,activation_fn=tf.nn.relu,scope="C_{}".format(i))
    i+=1

    out=conv_layers(out,size=1,rate=1,dropout_rate=hp.dropout_rate,activation_fn=tf.nn.relu,training=training,scope="C{}".format(i))
    i+=1

    out=highwayconvolution(out,size=3,rate=1,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1
    out=highwayconvolution(out,size=3,rate=3,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1
    out=highwayconvolution(out,size=3,rate=9,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1
    out=highwayconvolution(out,size=3,rate=27,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1

    out=highwayconvolution(out,size=3,rate=1,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1
    out=highwayconvolution(out,size=3,rate=3,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1
    out=highwayconvolution(out,size=3,rate=9,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1
    out=highwayconvolution(out,size=3,rate=27,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
    i+=1

    out=highwayconvolution(out,size=3,rate=1,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
     i += 1

    out=highwayconvolution(out,size=3,rate=1,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
     i += 1

     out=highwayconvolution(out,size=1,rate=1,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
      i += 1

     out=highwayconvolution(out,size=1,rate=1,dropout_rate=hp.dropout_rate,activation_fn=None,training=training,scope="HC_{}".format(i))
      i += 1

     K,V=tf.split(out,2,-1)
     return K,V

def AudioEnc(spec,training=True):
    i=1
    out=conv_layers(S,filters=hp.d,size=1,rate=1,padding="CAUSAL",dropout_rate=hp.dropout_rate,activation_fn=tf.nn.relu,training=training,scope="C_{}".format(i));
    i += 1
    out=conv_layers(S,filters=hp.d,size=1,rate=1,padding="CAUSAL",dropout_rate=hp.dropout_rate,activation_fn=tf.nn.relu,training=training,scope="C_{}".format(i));
    i += 1
    out=conv_layers(S,filters=hp.d,size=1,rate=1,padding="CAUSAL",dropout_rate=hp.dropout_rate,activation_fn=tf.nn.relu,training=training,scope="C_{}".format(i));
    i += 1

    out=highwayconvolution(out,size=3,rate=1,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
    out=highwayconvolution(out,size=3,rate=3,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
    out=highwayconvolution(out,size=3,rate=9,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
    out=highwayconvolution(out,size=3,rate=27,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1


    out=highwayconvolution(out,size=3,rate=1,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
    out=highwayconvolution(out,size=3,rate=3,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
    out=highwayconvolution(out,size=3,rate=9,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
    out=highwayconvolution(out,size=3,rate=27,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1

    out = highwayconvolutionc(tensor,size=3,rate=3,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1

    out = highwayconvolutionc(tensor,size=3,rate=3,padding="CAUSAL",dropout_rate=hp.dropout_rate,training=training,scope="HC_{}".format(i))
    i += 1
