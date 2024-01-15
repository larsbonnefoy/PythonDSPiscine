from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(0, 333, 33)):
    sleep(1)
print()
for elem in tqdm(range(0, 333, 33)):
    sleep(1)
print()
