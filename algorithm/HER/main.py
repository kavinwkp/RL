import argparse
from train import *
from test import *
import gymnasium as gym

parser = argparse.ArgumentParser()

parser.add_argument('--env_name',       type=str,   default='FetchPushDense-v2',  help='Fetch environment name')
parser.add_argument('--epochs',         type=int,   default=1000,            help='Number of epochs')
parser.add_argument('--timesteps',      type=int,   default=100,             help='number of iterations of network update')
parser.add_argument('--start_steps',    type=int,   default=5000,           help='initial number of steps for random exploration')
parser.add_argument('--max_ep_len',     type=int,   default=1000,            help='maximum length of episode')
parser.add_argument('--buff_size',      type=int,   default=int(1e6),        help='size of replay buffer')
parser.add_argument('--phase',          type=str,   default='test',          help='train or test')
parser.add_argument('--model_dir',      type=str,   default='./saved_models',help='path to model directory')
parser.add_argument('--test_episodes',  type=int,   default=5,              help='number of episodes testing should run')
parser.add_argument('--clip-obs',       type=float, default=200,             help='the clip ratio')
parser.add_argument('--clip-range',     type=float, default=5,               help='the clip range')
parser.add_argument('--lr_actor',       type=float, default=0.0001,          help='learning rate for actor')
parser.add_argument('--lr_critic',      type=float, default=0.001,           help='learning rate for critic')
parser.add_argument('--noise_scale',    type=float, default=0.1,             help='scaling factor for gaussian noise on action')
parser.add_argument('--gamma',          type=float, default=0.98,            help='discount factor in bellman equation')
parser.add_argument('--polyak',         type=float, default=0.999,           help='polyak value for averaging')
parser.add_argument('--cuda',           type=bool,  default=True,           help='whether to use GPU')
parser.add_argument('--her',            type=bool,  default=True,           help='whether to use HER')


args = parser.parse_args()

if args.phase == 'train':
    train_agent(args)
elif args.phase == 'test':
    test_agent(args)
else:
    print("Unknown phase. Enter train or test")
