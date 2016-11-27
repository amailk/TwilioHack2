#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from twilio import twiml

account_sid = "ACa6d65bfcb4ea7272014bb7ff9e5a7c8d"
auth_token  = "95f29e1c04ee7e398003eba871e928a7"
twilio_number = "+16474964327"

base = "http://twiliohack2.appspot.com"

GREETING = ''' "Hello. Please listen closely for the options. If you are calling because you have a question, please press 1. If you would like to register for our service, please press 2. If you would like to learn more about our service, please press 3.'''

class WelcomeHandler(webapp2.RequestHandler):


    def get(self):
        r = twiml.Response()
        with r.gather(action=base+"/choice", numDigits=1) as g:
            g.say(GREETING)

        self.response.write(r)

class ChoiceHandler(webapp2.RequestHandler):
    def post(self):
        choice = self.request.get("Digits")

        r = twiml.Response()
        r.say("You have entered, " + choice)
        self.response.write(r)

app = webapp2.WSGIApplication([
    ('/welcome', WelcomeHandler),
    ('/choice', ChoiceHandler),
], debug=True)
