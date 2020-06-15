# diceroller

Flask-based dice roller

## Running

1. Make sure you have installed Flask.
1. Open terminal or command prompt.
1. Navigate to where you have saved the roller file.
1. Enter `python diceroller.py` in terminal/command prompt.
1. Open the URL that appears in the browser of your choice.

## Usage

* *n***d***x*: Rolls *n* die with *x* sides.
* *n***d***x***ro***y*: Rolls *n* die with *x* sides, re-rolling the number *y* the first time it appears.
* *n***d***x***rr***y*: Rolls *n* die with *x* sides, re-rolling the number *y* every time it appears.
* *n***d***x***kh***y*: Rolls *n* die with *x* sides, keeping the highest *y* rolls.
* *n***d***x***kl***y*: Rolls *n* die with *x* sides, keeping the lowest *y* rolls.

## Goals

- [x] Make a basic dice roller
- [x] Add rerolling once functionality {diceroller.py}
- [x] Add multiple reroll functionality {diceroller.py}
- [x] Add keep highest roll(s) {diceroller.py}
- [x] Add keep lowest roll(s) {diceroller.py}
