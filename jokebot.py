import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hey there! I am a Joke Bot. You can ask me to tell you a random Joke that might just make your day better!" 
                       

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

    jokes = [
            " How does Moses make coffee? Hebrews it!"
            "I’m super friendly with 25 letters of the alphabet. I just don’t know why."
            "Did you hear about the guy whose whole left side was cut off? He’s all right now."
            "How many tickles does it take to make an octopus laugh? 10-tickles."
            "My leaf blower doesn’t work. It just sucks!"
            "How does an attorney sleep? First he lies on one side, then he lies on the other."
            "How do you invite a dinosaur for lunch? Tea, Rex?"
            "What do you call a dinosaur with one eye? A do-you-think-he-saur-us."
            "Is your iPad making you fall asleep? I can help—there’s a nap for that."
            "There was a kidnapping at school yesterday. Don’t worry, though—he woke up."
            "What do you call a girl with an hourglass figure? A complete waist of time."
            "I knew a mathematician who couldn’t afford lunch. He could binomial."
            "What did the mermaid wear to math class? An algae-bra."
            "What do you call a turtle who takes up photography? A snapping turtle."
            "You know what really bugs me? Insect puns."
            
           ]



class JokeIntentHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("JokeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = random.choice(jokes)
                       

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(JokeIntentHandler())


# Make sure IntentReflectorHandler is last so it
# Doesn't override your custom intent handlers

handler = sb.lambda_handler()




