# TypingTestAutoTyper
It's a short script that I made that uses the OCR (Optical Character Recognition) AI model to destroy typing tests with about 300wpm if it goes smoothly. It works by taking a screenshot, storing it in a folder and using the OCR module to translate the screenshot into string text. It then uses pyautogui to type said string.

You will most likely have to adjust the code for your own computer, but I think most of the code is thankfully self-explanatory enough. Pay extra attention to the pyautogui screenshot pixel dimensions, as that will probably differ based on screen dimensions at least somewhat.

Also feel free to steal this idea and try to use it for other tests like Nitrotype or typeracer, you most likely wouldn't have to change the code that much. Also maybe you could get it to take and process the screenshot while it's typing, instead of awkwardly pausing every 5 seconds. 
