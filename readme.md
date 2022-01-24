<img src="square-logo.svg" width=255 height=255 align="right">

#  Rasa 3.x Form Examples

This repository is part of our Rasa Forms course that's hosted on our [learning center](https://learning.rasa.com/).

## Installation 

To run all the examples here you'll need to install Rasa, preferably in a virtualenv in the root directory. 

```
python -m pip install rasa==3.0
```

## 1. Custom Actions

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

Code can be found in the `01-actions` folder.

## 2. Slots 

It helps to understand custom actions and slots before we talk about forms. In this simple bot we show how they work by keeping track of a users name. 

Code can be found in the `02-slots` folder.

## 3. Simple Forms with Conditional Slots

If we want to query multiple things from the user, it may be best to use forms instead of custom actions. Luckily for us, we can use our `RulePolicy` to help us out and we can configure our slots to ignore entities mentioned outside of our form.

Code can be found in the `03-conditions` folder. 

## 4. From Text

You can fill slots from many types of input, this includes raw text! 

Code can be found in the `04-from-text` folder.

## 5. Form Validation 

What if we want to validate the input of our form? We don't want to have a name that's an empty string after all! 

Code can be found in the `05-validation` folder.
