from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-394902393764-396202078743-395141031122-8999cebe2c5905be0e0753786c89348e', 
		            'xoxb-394902393764-395141032434-oZgCi1tiDnzJjeZ8NJYGqZdF', 
			    'WiNi5l2Yq8tiGgGNHvx33YZr', 
			    True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))
