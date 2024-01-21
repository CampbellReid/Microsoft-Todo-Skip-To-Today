
# Microsoft Todo Task Skipper

It is a simple window which opens and allows you to quickly skip old outdated tasks to today.


## Setup the environment

Clone the project

```bash
  git clone https://github.com/RamboCambo/Microsoft-Todo-Skip-To-Today
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  conda create -n todoapp -f requirements.txt
```

Activate the environment

```bash
  conda activate todoapp
```

## Run the program

Run the click.py program

```bash
  python click.py
```

Open the Todo app and click on the top box somewhere in the red square

![Obfuscated image showing where to click and get the coordinates](/Example.png)

Copy the coordinates from the console and pass in as --click_x= and --click_y=

```bash
  python main.py --click_x=<your x> --click_y=<your y>
```

Move the opened window to the side so it doesn't get in the way

Click the first item in the list so you start with the sidebar open otherwise it won't work.

Now for each item you want to skip to today, click the button on the popup window.
