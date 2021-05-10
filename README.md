# DaVinki 

Something to automate my repetitive photo editing process since I've got no idea what I'm doing, 
and a computer can achieve that faster.

At the moment it only increases the saturation and contrast by some arbitrary values that seem to work _okay_.

## How to steal this 

First of all, _why_??

If you _really_ need to run this, make sure you've got Python >3.6 installed.

After you've cloned the repository, create a virtual environment (i.e. run this shenanigan in your terminal of choice):

```shell
python3 -m venv venv
```

Activate it:

* windows (powershell) - ```.\venv\Scripts\Activate.ps1```
* *nix - ```source ./venv/bin/activate ```

Install the requirements:

```shell
pip install -r requirements.txt
```

Export environment variables:

```shell
export input_directory=/absolute/path/to/directory/of/choice
export output_directory=/absolute/path/to/directory/of/choice
```

Might make an actual interface for this - until then, you'll have to _suffer_.

Finally, you can run it: ```python3 main.py``` 

## WIP

* actual exposure / black levels
* tweak filter values via a config file or something
* _smarter_ editing 
* editing 'profiles' (save a preset of filter values and load it as you please)


Feel free to raise an issue with any feature you'd like to see in this.