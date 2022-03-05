# SchoolMeet

A small program to automatically login to Google Meet when Morning Exercise.

Default school has been set to "nkhhs"

## Building

### Requirements

* Python 3.10.1+
* selenium 4.1.2+
* Chrome 90+

### Setup

1. Fork and clone this repositorie or download the .zip file.

    **(Optional)** In `SchoolMeet` (or `SchoolMeet-master`) folder, create a virtual environment.

    ```bat
    virtualenv .venv -p <path to Python 3.10.1 interpreter>
    ```

2. Install requriments.

    ```bat
    pip install -r requriments.txt
    ```

### Packaging

* You can use this command to package the author-optimized applications.

    ```bat
    pyinstaller -s build.spec && copy src/chromedriver.exe dist/SchoolMeet
    ```

* Or custom

    ```bat
    pyinstaller GUI.py <some args> && copy src/chromedriver.exe dist/SchoolMeet
    ```

**You should put `chromedriver.exe` to the folder what packaged application is in.**

## Contribute

1. Fork
2. Write Code
3. Send Pull Request
4. Report issues

PM me

* Discord : KSHSlime#9034
* Email : iceice666@outlook.com (I will check email about twice a week, probably😅)

## License

MIT License
