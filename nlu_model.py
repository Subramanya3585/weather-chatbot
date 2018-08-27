from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

args = {"pipeline":"spacy_sklearn","name":"nlp_spacy","name":"ner_crf","name":"ner_synonyms","name":"intent_classifier_tensorflow_embedding","path":"./models/nlu","data":"./data/data.json"}

def train_nlu(data, args, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.RasaNLUModelConfig(args))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')

def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/weathernlu')
    print(interpreter.parse(u"what about kochi"))	

if __name__ == '__main__':
	#train_nlu('data/data.json', args, './models/nlu')
    run_nlu() 