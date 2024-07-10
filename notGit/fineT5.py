from sklearn.model_selection import train_test_split

from transformers import T5Tokenizer, T5ForConditionalGeneration  

from transformers import AdamW
import pandas as pd
import torch
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint
from torch.nn.utils.rnn import pad_sequence
# from torch.utils.data import Dataset, DataLoader, random_split, RandomSampler, SequentialSampler

pl.seed_everything(100)
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("/kaggle/input/3k-conversations-dataset-for-chatbot/Conversation.csv")
data.drop(columns=['Unnamed: 0'],inplace=True)
print("No of rows:" ,data.shape[0])