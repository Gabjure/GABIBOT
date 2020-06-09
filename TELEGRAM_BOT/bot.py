"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Deployed using heroku.

Author: liuhh02 https://medium.com/@liuhh02
"""

import nltk
nltk.download('punkt')

import tensorflow as tf
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

encoder_model = load_model('encoder_model_500e_8kl', compile=False)
with tf.device('/cpu:0'):
    encoder_model.compile(loss='categorical_crossentropy', optimizer='adam')

decoder_model = load_model('decoder_model_500e_8kl', compile=False)
with tf.device('/cpu:0'):
    decoder_model.compile(loss='categorical_crossentropy', optimizer='adam')

import pickle
with open('input_word2idx_500e_8kl.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    input_word2idx = pickle.load(f)

with open('target_word2idx_500e_8kl.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    target_word2idx = pickle.load(f)

input_word2idx['PAD'] = 0
input_word2idx['UNK'] = 1
target_word2idx['UNK'] = 0
input_idx2word = dict([(idx, word) for word, idx in input_word2idx.items()])
target_idx2word = dict([(idx, word) for word, idx in target_word2idx.items()])

num_encoder_tokens = len(input_idx2word)
num_decoder_tokens = len(target_idx2word)

import os
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1239797018:AAEq1ye6YkGbaUmi__QEeXO0VC6SNRAKH4Q'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def reply(update, context):
    """Echo the user message."""
    input_text = update.message.text

    try:
    
        input_seq = []
        input_wids = []
        max_encoder_seq_length = 15
        max_decoder_seq_length = 20

        for word in nltk.word_tokenize(input_text.lower()):
            idx = 1
            if word in input_word2idx:
                idx = input_word2idx[word]
            input_wids.append(idx)

        input_seq.append(input_wids)
        input_seq = pad_sequences(input_seq, max_encoder_seq_length)
        states_value = encoder_model.predict(input_seq)
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, target_word2idx['START']] = 1
        target_text = ''
        target_text_len = 0
        terminated = False

        while not terminated:
            output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
            sample_token_idx = np.argmax(output_tokens[0, -1, :])
            sample_word = target_idx2word[sample_token_idx]
            target_text_len += 1

            if sample_word != 'START' and sample_word != 'END':
                target_text += ' ' + sample_word

            if sample_word == 'END' or target_text_len >= max_decoder_seq_length:
                terminated = True

            target_seq = np.zeros((1, 1, num_decoder_tokens))
            target_seq[0, 0, sample_token_idx] = 1

            states_value = [h, c]

        update.message.reply_text(target_text.strip().replace('UNK', ''))

    except Exception as e:
        print(e)
        update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main_poll():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, reply))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def main_hook():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary	
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://agile-waters-31590.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main_poll()
