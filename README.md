## Synopsis

dice2mnemonic is a python script that provides a way to create BIP39 mnemonic phrases from
N-sided dice (2 sides or more). The algorithm is provably fair, including the
choice of the checksum word at the end.

## requirements

This makes use of the python-mnemonic library found here:

https://github.com/trezor/python-mnemonic

## Example:

```$ python3 dice2mnemonic.py 
seed length? (12,15,18,21,24): 24
dice # of sides: 6
roll: 1
roll: 3
roll: 5
roll: 1
roll: 2
found word:  abandon
roll: (continues for quite some time here, keep rolling)
...

seed phrase:
abandon rug truck segment air tenant raise piano physical try trust crime
```


## License

MIT
