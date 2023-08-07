# Monopoly Bank Simulator
One evening when I gathered my cousins to play Monopoly, I found that the electronic bank used to do transactions wasn't working. Instead of moving to another game, I got an idea - why not code it?

## What does the electronic bank do?
It is a device that has 2 slots where you can insert your monopoly card. A player can either spend money, collect money or transfer money to another player using the bank. The bank has a digital screen which displays the player's balance once the card is inserted into the slot.

## How my coded bank works
When you run `bank.py` in your terminal, it first asks you the number of players followed by their names and card colours (optional)\
Once this is done, you will be prompted with  `Enter command:` 

- Spend
  `playerName.spend(amount)` deducts `amount` from `playerName`'s balance
- Collect
  `playerName.collect(amount)` adds `amount` to `playerName`'s balance
- Transfer
  `playerA.transfer(playerB, amount)` transfers `amount` from `playerA` to `playerB`
- Check balance
  `playerName.balance` prints `playerName`'s balance
- Player transaction history
  `playerName.history` prints all the transactions done by `playerName` (also includes transactions where `playerName` has receieved money from another player)
- Ledger
  `ledger` prints all the transactions that took place since the beginning

## Extra feature 
I have added an extra feature which is that all players' balance is stored in a `.txt` file and is updated after every command you enter. To specify the location where you want to save the text file, upadte the `path` variable in 
