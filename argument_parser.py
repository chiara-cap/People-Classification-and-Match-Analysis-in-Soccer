import argparse     # parsing elements from command line


def get_args():
    # Creating an object that will contain the information given from the command line
    parser = argparse.ArgumentParser()

    # Dataset
    parser.add_argument('--data-path', default='/mnt/beegfs/work/cvcs_2022_group20/SoccerNet-v3', help='dataset')
    parser.add_argument('--split', type=str, default='train', help='train or test')
    parser.add_argument('--output-dir', type=str, default='', help='directory where to save results, empty if no saving')
    parser.add_argument('--task', type=str, help='detection, geometry or retrieval')
    parser.add_argument('--epochs', default=10, type=int)
    parser.add_argument('-b', '--batch-size', default=4, type=int)
    parser.add_argument('--tiny', required=False, type=int, default=None, help='Select a subset of x games')

    # Model
    parser.add_argument('--pretrained', action='store_true', default=True, help='use pretrained backbone')
    parser.add_argument('--tl', default=0.9, type=float, help='Value for tau_low (default: 0.9')
    parser.add_argument('--th', default=1., type=float, help='Value for tau_high (default: 1.)')

    # Optimizer
    parser.add_argument('--momentum', default=0.9, type=float, help='momentum')
    parser.add_argument('-wd', '--weight-decay', default=1e-4, type=float, help='weight decay (default: 1e-4)')
    parser.add_argument('--lr', default=0.01, type=float, help='initial learning rate')

    args = parser.parse_args()
    return args
