# Video Trimmer

This script allow the user to trimm videos using _"moviepy"_ python module by providing the complete path and name to the video and specify a start and end time in the _"config.yaml"_.

# Steps

Create a python enviroment

```
python -m venv .env
```

Activate the new environment and install requirements

```
source .env/Scripts/activate
pip install -r requirements.txt
```

Open _"config.yaml"_ and edit the following keys:

**path:** Complete path to the video.

**start:** The start time to trim from, format _"hh:mm:ss"_.

**end:** The end time to trim to, format _"hh:mm:ss"_.
<br>
<br>

### **Run the script**

```
python main.py
```
