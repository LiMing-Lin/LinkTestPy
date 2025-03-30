import torch


if __name__ == '__main__':
    load_dict = torch.load('./data/Cora/processed/data.pt')
    print(load_dict)