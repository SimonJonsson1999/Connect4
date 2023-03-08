import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np

def create_model(row,col):
    model = keras.models.Sequential([
        layers.Dense(row*col, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(50, activation='relu'),
        layers.Dense(7)
    ])
    return model
   

def compute_loss(logits, actions, rewards): 
    neg_logprob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=actions)
    loss = tf.reduce_mean(neg_logprob * rewards)
    return loss
  
def train_step(model, optimizer, observations, actions, rewards):
    with tf.GradientTape() as tape:
      # Forward propagate through the agent network
        
        logits = model(observations)
        loss = compute_loss(logits, actions, rewards)
        grads = tape.gradient(loss, model.trainable_variables)
        
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

def get_action(model, observation, epsilon):
    #determine whether model action or random action based on epsilon
    act = np.random.choice(['model','random'], 1, p=[1-epsilon, epsilon])[0]
    observation = np.array(observation).reshape(1,6,7,1)
    logits = model.predict(observation)
    prob_weights = tf.nn.softmax(logits).numpy()
    
    if act == 'model':
        action = list(prob_weights[0]).index(max(prob_weights[0]))
    if act == 'random':
        action = np.random.choice(7)
        
    return action, prob_weights[0]