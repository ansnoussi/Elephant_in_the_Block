# Elephant in the Block

Elephant in the block is a CLI tool that will alert you each time a transaction is made on the Bitcoin blockchain that surpasses **1 Million Dollars**.

| Basic Usage  | Verbose mode |
| ------------- | ------------- |
| <img src="https://i.imgur.com/m8SoDjD.png">  | <img src="https://i.imgur.com/Gbz35Di.png">  |
## FAQ

<details>
<summary> <b> Why? </b> </summary>
Because it's fun, and exciting to a certain extent.
</details>

<details>
<summary> <b> What does 'Elephant' mean? </b> </summary>
I find it really interesting how elphants hold tails when walking in a line (just like a blockchain right ?), so this tool is called Elephant in the block because it will help you catch that big Elephant.
<img src="https://i.imgur.com/Phgx3Sm.jpeg">
</details>

## Run in a Virtualenv

1. create a Virtualenv : `virtualenv venv`
2. connect to it : `source venv/bin/activate`
3. install from requirements file : `pip install -r requirements.txt`
4. generate requirements file : `pip freeze —local > requirements.txt`
5. disconnect from Virtualenv : `deactivate`

## Usage
```
Usage: elephant.py [OPTIONS]

  Get alerted each time a transaction is made on the Bitcoin blockchain that
  surpasses 1 Million Dollars.

Options:
  -v, --verbose      Print more output.
  --ammount INTEGER  Ammount in $ to listen for (default 1000000).
  --help             Show this message and exit.
```