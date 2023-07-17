import speech_recognition as sr

r = sr.Recognizer()

while True:
        # Exception handling to handle exceptions at the runtime if
        # no user prompt given
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                print("Microphone is open now say your prompt...")
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                my_prompt = r.recognize_google(audio2)
                my_prompt = my_prompt.lower()

                print("Did you say :", my_prompt)
                

        except Exception as e:
            print(e)
            print("Could not request results; {0}".format(e))